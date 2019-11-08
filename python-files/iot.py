import json


lol=''
try:

	with open('i.json', 'r') as jsonFile:
		lol = json.load(jsonFile)
		pass

finally:
	if (jsonFile):
		jsonFile.close()

def getEmail(imageName):
	for key in lol['user']:

		if (imageName == key['image']):
			email = key['email']
			print(email)

getEmail('tuukka.jpg')
