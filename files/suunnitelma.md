# Suunnitelma

```python
From serializer import Serializer
Import time
Class facerec :


	__init__(self):
		pass
	

	main_facerec(self)
	#waits for someone to appear, takes a picture, saves the picture, calls authentication with 	picture name (timestamp) as parameter

	handle_auth(self, picture-name)
	# compares picture to known pictures of users
	user = serializer.deserialize(picture-name)
	# call 2fa to confirm auth
	returns result: user or None

	post_auth
	#greets user
	#calls IoT depending on authorization

Class user:
import serializer
	__init__:
		self.__name = 
		self.__image #absolute path
		self.__email

	@property
	def name(self)
	return self.__name
	
	def create_user(self):
		# selialize the user
	
		
Class 2fa:

	def send_email(self)


Class IoT:
	pass


Class serializer:
	#from Tuukka
```