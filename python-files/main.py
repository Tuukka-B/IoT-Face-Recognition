#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Created on Thu Nov 14 18:32:12 2019

@author: team IoT
"""

import auth
import facerec
import json
import sys
if __name__ == '__main__':
    jsonloc = "./../files/json.json"
    #known_img_dir = ""
    recognised = "Unknown"
    count = 0
    jsondata = ""
    with open(jsonloc,"r") as jsonfile:
        data = jsonfile.read()
        #sys.exit(1)
        jsondata = json.loads(data)
        #print(jsondata["user"]["Tuukka"]["email"])
    #sys.exit(1)
    while True:
        # mainloop, waits to recognise a face
        #######################################################################
        
        #variable for recognising failed authentication attempts
        old = recognised
        recognised = facerec.facerec()
        if "list" in type(recognised):
            # multiple recognitions happened... choosing the primary one (first)
            recognised = recognised[0]
        
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
        while count < 3 and recognised != "Unknown":
            #generates key
            #authenticate the recognised user
            email = ""
            try:
                email = jsondata["user"][recognised]["email"]
            except:
                print(f"User named {recognised} was not found from the database!\Exiting authentication...")
                break
            key = auth.key()
            auth.sendEmail(email, key)
            auth = auth.readEmail(key)
            if auth == False:
                count+=1
                #goes back to facerec stage
                break
            
            #greet the guest
            print(f"Hello {recognised}!")
            
            #reinitializes variables that track failed attempts
            count = 0
            old = "Unknown"
            # TO-DO: TTS voice greeting
        
        
            # IoT commands to ESP32
            ###################################################################
            
            """
            some stuf
            """
            
            #after IoT commands, let's go back to the mainloop
            break
        