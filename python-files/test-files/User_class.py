


class User:
    def __init__(self,id,name,image,email):
        self.__name=name
        self.__image=image
        self.__email=email
    @property
    def name(self):
        return self.__name
        
    @property    
    def image(self):
        return self.__image
        
    @property
    def email(self):
        return self.__email
    
    def set_name(self,x):
        self.__name=x
    
    def set_image(self,x):
        self.__image=x
    
    def set_email(self,x):
        self.__email=x

