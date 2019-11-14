#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Created on Thu Nov 14 18:32:12 2019

@author: team IoT
"""

import auth
#import facerec
import json
import sys
if __name__ == '__main__':
    jsonloc = "./../files/json.json"
    #known_img_dir = ""
    recognised = "Unknown"
    count = 0
    with open(jsonloc,"r") as jsonfile:
        data = jsonfile.read()
        #sys.exit(1)
        jsondata = json.loads(data)
        print(jsondata["user"]["Tuukka"]["email"])
#        for val in jsondata:
#            for count in range(0, len(val)):
#                print(val[count])
    sys.exit(1)
    while True:
            
        # mainloop, waits to take a picture
        ######################################################################
        old = recognised
        recognised = facerec.facerec()
        if "list" in type(recognised):
            # multiple recognitions happened... choosing the primary one (first)
            recognised = recognised[0]
            
        if recognised == old:
            count+=1
        if count > 2:
            # PLAY THE ALARM!!! WE HAVE AN INTRUDER
            # we could even do an alarm function with emails and stuff that
            # has to be deactivated manually by code....
            pass
        
        # auth loop, does the authentication
        ######################################################################
        # attempts are capped at 3 (first attempt is not logged)
        while count < 3 and recognised != "Unknown":
            for val in json:
              pass  
            key = auth.key()
            auth.sendEmail(jsondata["user"][recognised]["email"], key)
            auth = auth.readEmail(key)
            if auth == False:
                count+=1
                #goes back to facerec stage
                break
            
            #greet the guest
            print(f"Hello {recognised}!")
            count = 0
            old = "Unknown"
            # TO-DO: tts voice greeting
        
        
        # IoT commands to ESP32
        ######################################################################
        
        
        