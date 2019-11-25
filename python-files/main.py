#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Created on Thu Nov 14 18:32:12 2019

@author: team IoT
"""

import auth
import json
#import sys
import cl_facerec
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
        #print(jsondata["user"]["Tuukka"]["email"])
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
        if count > 2:
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
            auth.sendEmail(email, avain)
            input("email: >")
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
        
        
            # IoT commands to ESP32
            ###################################################################
            
            """
            some stuf
            """
            
            #after IoT commands, let's go back to the mainloop
            break
        
