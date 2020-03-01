#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 16:08:16 2019

@author: team IoT
"""

import face_recognition
import picamera
import os
import time
#import io
import numpy
import grove
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
        self.__tuukka_image = face_recognition.load_image_file("tuukka.jpg")
        self.__samson_image = face_recognition.load_image_file("samson.jpg")
        self.__jaber_image = face_recognition.load_image_file("jaber.jpg")
        try:
            self.__tuukka_face_encoding = face_recognition.face_encodings(self.__tuukka_image)[0]
            self.__samson_face_encoding = face_recognition.face_encodings(self.__samson_image)[0]
            self.__jaber_face_encoding = face_recognition.face_encodings(self.__jaber_image)[0]
        except IndexError:
            #unrecognisable faces in known face encodings
            print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
            quit()
        self.__known_faces = [
                self.__tuukka_face_encoding,
                self.__samson_face_encoding,
                self.__jaber_face_encoding
        ]
        self.__timestamp = None
        self.__camera = picamera.PiCamera()
        self.__camera.resolution = (320, 240) #lower the resolution to make it faster
        self.__capture = numpy.empty((240, 320, 3), dtype=numpy.uint8)
    # Load the jpg files into numpy arrays
    def compare(self):
        try:
            #__capture = numpy.empty((240, 320, 3), dtype=numpy.uint8) 
            # above to make it even more faster
            self.__camera.start_preview(fullscreen=False,window=(100,200,300,400))
            """
            nappi = None
            nappi = input('Ota kuva (näppäin + enter = ota kuva, q + enter = poistu) > ')
            if nappi == 'q':
                return None
            """
            grove.button()
            self.__timestamp = time.strftime("%Y-%m-%d_%H:%M:%S")
            #camera.capture(__capture, format = 'rgb') #if we really want fast...
            # but this doesn't save images to disk...
            #camera.capture(path)
            """new code"""
            #stream = io.BytesIO() obsolete
            # capture into stream
            self.__camera.capture(self.__capture, format='rgb')
            # convert image into numpy array
            #self.__image_data = numpy.fromstring(stream.getvalue(), dtype=numpy.uint8) #obsolete
            """end new code"""
            
            self.__camera.stop_preview()
            
            """ new"""
            unknown_image = self.__capture # new way
            """end new"""
            #unknown_image = face_recognition.load_image_file(path) #old way
            #unknown_encoding = face_recognition.face_encodings(unknown_image)[0] #old way
            unknown_encoding = face_recognition.face_encodings(unknown_image) #NEW!
            # results is an array of True/False telling if the unknown face matched anyone in the known_faces array
            recognition = "None"
            """DEBUGGING CODE
            while True:
                num = input("choose an image to compare to:\n0 = tuukka, 1 = samson, 2 = jaber, 'q' to quit\n")
                if num == "q":
                    return None
                else:
                    try:
                        num = int(num)
                    except Exception:
                        print("Invalid command,please input a number to continue or 'q' to quit.")
                        continue
                results = face_recognition.compare_faces(self.__known_faces[num], unknown_encoding)
                print(("comparison result, {}").format(results))
            DEBUGGING CODE ENDS"""
            count = 0
            for count in range(0,3):
                results = face_recognition.compare_faces(self.__known_faces[count], unknown_encoding)
                if results[0] == True:
                    #recognition = self.__known_faces.index(face_encoding)
                    #print(("face recognised at index '{}', real index should be {}").format(recognition, count))
                    recognition = count
                count += 1
            
            print("Is the unknown face a picture of Tuukka {}".format(recognition == 0))
            print("Is the unknown face a picture of Samson? {}".format(recognition == 1))
            print("Is the unknown face a picture of Jaber? {}".format(recognition == 2))
            print("Is the unknown face a new person that we've never seen before? {}".format(recognition  == 'None'))
            if recognition == 0:
                return "Tuukka"
            elif recognition == 1:
                return "Samson"
            elif recognition == 2:
                return "Jaber"
            #TO-DO: Add Arttu
            else:
                return None
            
        except Exception:
            print("error in face recognition, exiting...")
            return "error"
        
    def save_img(self):
        from PIL import Image
        filename = self.__timestamp + ".jpg"
        imgpath = os.path.join(self.__unknown_img_dir, filename)
        self.__capture.transpose()
        img = Image.fromarray(self.__capture, 'RGB')
        #reinitialialization of __capture
        self.__capture = numpy.empty((240, 320, 3), dtype=numpy.uint8)
        img.save(imgpath)
        
#if __name__ == "__main__"
#    p = cl_facerec("./", "./unknown/")
#    p.compare()
