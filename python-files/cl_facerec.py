#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 16:08:16 2019

@author: team IoT
"""

import face_recognition
import picamera
import os

class facerec :
    
    def __init__(self, known_img_dir, unknown_img_dir):
        if not os.path.exists(known_img_dir):
            print("Invalid directory given, exiting...")
            quit()
        if not os.path.exists(unknown_img_dir):
            try:
                print(("directory for unknown images does not exist, creating one to '{}'...").format(unknown_img_dir))
                os.mkdir(unknown_img_dir)
            except Exception:
                print("could not make a directory for unknown images, exiting...")
                quit()
        self.__unknown_img_dir = unknown_img_dir
        self.__known_img_dir = known_img_dir
        self.__count = 0
        self.__tuukka_image = face_recognition.load_image_file("tuukka.jpg")
        self.__samson_image = face_recognition.load_image_file("samson.jpg")
        self.__jaber_image = face_recognition.load_image_file("jaber.jpg")
        try:
            self.__tuukka_face_encoding = face_recognition.face_encodings(self.__jaber_image)[0]
            self.__samson_face_encoding = face_recognition.face_encodings(self.__samson_image)[0]
            self.__jaber_face_encoding = face_recognition.face_encodings(self.__jaber_image)[0]
        except IndexError:
            print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
            quit()
        self.__known_faces = [
                self.__tuukka_face_encoding,
                self.__samson_face_encoding,
                self.__jaber_face_encoding
        ]
# Load the jpg files into numpy arrays
def compare(self):
    
    camera = picamera.PiCamera()
    camera.start_preview(fullscreen=False,window=(100,200,300,400))
    
    nappi = None
    path = None
    while nappi != 'c':
        nappi = input('Ota kuva (c = ota kuva, q = poistu) > ')
    
        if nappi == 'q':
            break
        filename = self.__count + ".jpg"
        path = os.path.join(self.__unknown_img_dir, filename)
        self.__count += 1
        camera.capture(path)
        
    unknown_image = face_recognition.load_image_file(path)  
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
    camera.stop_preview()
    # results is an array of True/False telling if the unknown face matched anyone in the known_faces array
    results = face_recognition.compare_faces(self.__known_faces, unknown_encoding)
    
    print("Is the unknown face a picture of Tuukka {}".format(results[0]))
    print("Is the unknown face a picture of Samson? {}".format(results[1]))
    print("Is the unknown face a picture of Jaber? {}".format(results[2]))
    print("Is the unknown face a new person that we've never seen before? {}".format(not True in results))
    if results[0]:
        return "Tuukka"
    elif results[1]:
        return "Samson"
    elif results[2]:
        return "Jaber"
    #TO-DO: Add Arttu
    else:
        return None