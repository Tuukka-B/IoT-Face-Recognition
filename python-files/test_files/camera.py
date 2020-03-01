import picamera
import argparse
import time
import face_recognition


parser = argparse.ArgumentParser()
parser.add_argument('filename')

args = parser.parse_args()
camera = picamera.PiCamera()
camera.start_preview(fullscreen=False,window=(100,200,300,400))

nappi = 'c'

while nappi == 'c':
    nappi = input('Ota kuva (c = ota kuva, q = poistu) > ')

    if nappi == 'q':
        break
    
    camera.capture(args.filename)
    known_image = face_recognition.load_image_file("samson.jpg")
    unknown_image = face_recognition.load_image_file(args.filename)

    image_encoding = face_recognition.face_encodings(known_image)[0]
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

    results = face_recognition.compare_faces([image_encoding], unknown_encoding)

    print(results)

camera.stop_preview()
