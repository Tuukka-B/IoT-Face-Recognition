


```python

class User:
    def __init__(self,name,image,email):
        self.__name=name
        self.__image=image
        self.__email=email
    @property
    def name(self):
        return self.__name
    
    def set_name(self,x):
        self.__name=x

   ```