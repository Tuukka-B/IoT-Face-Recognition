#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 13:12:37 2019

@author: team IoT (Jaber, Tuukka, Samson, Arttu)
"""
import json
import time
class facerec :


    def	__init__(self):
    		pass
    	
    
    def	main_facerec(self):
    	#waits for someone to appear, takes a picture, saves the picture, calls authentication with 	picture name (timestamp) as parameter
        pass
    
    def	handle_auth(self, picture_name):
        pass
    	# compares picture to known pictures of users
    	# call 2fa to confirm auth
        
    	#return result: user or None
    
    	#post_auth:
    	#greets user
    	#calls IoT depending on authorization

class user:
	def __init__(self):
		self.__name = ""
		self.__image = "" #absolute path
		self.__email = ""

	@property
	def name(self):
        return self.__name
	
	def create_user(self):
		# selialize the use
        pass
	
		
class 2fa:
    def __init__(self):
        
	def send_email(self):
        pass

def IoT(conn, command):
	pass
