from typing import TypedDict

class person(TypedDict):
    name:str
    age:int

#In class we define age an int but when we create new class we write age as a string 
#but still it will run without any error

new_person:person={'name':'dil','age':"21"}
print(new_person)