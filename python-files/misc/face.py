import picamera
import time
import face_recognition
import auth
import json
import os
import time
#import io
import numpy

#loading kssown peaple's images
tuukka_image = face_recognition.load_image_file("./known/tuukka.jpg")
samson_image = face_recognition.load_image_file("./known/samson.jpg")
jaber_image = face_recognition.load_image_file("./known/jaber.jpg")


#encoding known peaple's images
try:
    tuukka_face_encoding = face_recognition.face_encodings(tuukka_image)[0]
    samson_face_encoding = face_recognition.face_encodings(samson_image)[0]
    jaber_face_encoding = face_recognition.face_encodings(jaber_image)[0]
except IndexError:
    print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
    quit()

# array of known peaple
known_faces = [tuukka_face_encoding,samson_face_encoding,jaber_face_encoding]

count = 0

while True:
    camera = picamera.PiCamera()
    camera.start_preview(fullscreen=False,window=(100,200,300,400))

    nappi = 'c'

    if nappi == 'c':
        nappi = input('Ota kuva (c = ota kuva, q = poistu) > ')

        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        pic="./unknown/"+timestamp+".jpg"
        camera.capture(pic)
        unknown_image = face_recognition.load_image_file(pic)
        unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
    camera.stop_preview()


    person="unknown"
    
    for x in range(3):
        results = face_recognition.compare_faces([known_faces[x]], unknown_encoding)
        
        if results[0]==True:
            if x==0:
                person="Tuukka"
            elif x==1:
                person="Samson"
            elif x==2:
                person="Jaber"

    if person!="unknown":
        print("Welcome "+person+"! Please wait while sending an email to you for your identity confirmation!")
        
        jsonloc = "./db.json"
        jsondata = ""
        with open(jsonloc,"r") as jsonfile:
            data = jsonfile.read()
            jsondata = json.loads(data)

        while count < 3:
            #generates key
            #authenticate the recognised user
            email = ""
            try:
                email = jsondata["user"][person]["email"]
            except:
                print(("User named '{}' was not found from the database!\nExiting authentication").format(person))
                break
            key = auth.key()
            auth.sendEmail(email, key)
            input("Email >")
            auth = auth.readEmail(key)
            if auth == False:
                count+=1
                #goes back to facerec stage
                break

            count = 0 
            break
    else:
        count+=1
        print("Sorry! could not recognize you! Try again!")
