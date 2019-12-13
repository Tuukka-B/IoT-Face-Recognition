#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Created on Thu Nov 14 18:32:12 2019

@author: team IoT
"""

import auth
import json
import esp32client
import time
import grove
#import sys
import cl_facerec
from _thread import *
if __name__ == '__main__':
    jsonloc = "./../files/db.json"
    known_img_dir = "./"
    unknown_img_dir = "./unknown/"
    recognised = None
    count = 0
    jsondata = ""
    p = cl_facerec.facerec(known_img_dir, unknown_img_dir)
    with open(jsonloc,"r") as jsonfile:
        data = jsonfile.read()
        jsondata = json.loads(data)
    while True:

        # mainloop, waits to recognise a face
        #######################################################################
        
        #variable for recognising failed authentication attempts
        old = recognised

        recognised = p.compare()
        print(recognised)
        #increasing the counter of failed attempts
        if recognised == old:
            count+=1
        else:
            count = 0
            
        """grove buzzer test"""
        if (count > 2 or recognised is None) and recognised != "error":
            p.save_img()
            grove.buzzer()
            #time.sleep(2)
            #exit()
        # PLAY THE ALARM!!! WE HAVE AN INTRUDER
        # we could even do an alarm function with emails and stuff that
        # has to be deactivated manually by code....
        pass
        
        # auth loop, does the authentication
        #######################################################################
        
        # attempts are capped at 3 (first attempt is not logged)
        while count < 3 and recognised != None:
            #generates key
            #authenticate the recognised user
            email = ""
            try:
                email = jsondata["user"][recognised]["email"]
                print(email)
            except:
                print(("User named '{}' was not found from the database!\nExiting authentication").format(recognised))
                break
            avain = auth.key()
            print("Key created. Sending email!")
            auth.sendEmail(email, avain)

            #input("email: >")
            print("Email sent. Reading email! wait!")

            au = auth.readEmail(avain)
            if au == False:
                count+=1
                #goes back to facerec stage
                break
            
            #greet the guest
            print(("Hello {}!").format(recognised))
            
            #reinitializes variables that track failed attempts
            count = 0
            old = None
            # TO-DO: TTS voice greeting
        
            #print("ESP is commented out from code")
            # IoT commands to ESP32
            ###################################################################


            print("sending command to ESP32 to light the led...")

            esp32client.sendData('1')
            time.sleep(5)
            print("Powering off the led...")
            esp32client.sendData('0')
            
            #after IoT commands, let's go back to the mainloop
            break
        
