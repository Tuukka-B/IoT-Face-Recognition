#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 11:58:33 2019

@author: team IoT

Install instructions:
    sudo curl -kL dexterindustries.com/update_grovepi | bash
    sudo reboot
    
Update grove firmware:
    cd Desktop/GrovePi/Software/Python/
    sudo python grove_firmware_version_check.py
    cd /home/pi/Desktop/GrovePi/Firmware
    sudo chmod +x firmware_update.sh
    sudo ./firmware_update.sh
    
Updating the github directory:
    cd /home/pi/Desktop/GrovePi
    sudo git fetch origin
    sudo git reset --hard
    sudo git merge origin/master
"""
import grovepi

def button():
    # Connect the Grove Button to digital port D3
    # SIG,NC,VCC,GND
    button = 3

    grovepi.pinMode(button,"INPUT")
    press = 0
    while True:
        try:
            press = grovepi.digitalRead(button)
            if press == True:
                return True
    
        except IOError:
            print ("Error")

def buzzer():
    import time

    # Connect the Grove Buzzer to digital port D8
    # SIG,NC,VCC,GND
    buzzer = 8
    s = 0
    
    grovepi.pinMode(buzzer,"OUTPUT")
    
    while s < 2:
        try:
            # Buzz for 1 second
            grovepi.digitalWrite(buzzer,1)
            #print ('start')
            time.sleep(1)
    
            # Stop buzzing for 1 second and repeat
            grovepi.digitalWrite(buzzer,0)
            #print ('stop')
            time.sleep(1)
            
            s += 1
    
        except KeyboardInterrupt:
            grovepi.digitalWrite(buzzer,0)
            break
        except IOError:
            print ("Error")
            
        # Could make a thread / queue for the buzzer so it does not 
        # interrupt other functions
"""
if __name__ == '__main__':
    choice = input("choose a function/n'1': button/n'2': buzzer")
    if choice == '1':
        button()
    if choice == '2':
        buzzer()
"""