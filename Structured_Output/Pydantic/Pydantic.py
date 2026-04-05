#Pydantic is a data validation and data parsing library for python
#It ensures that the data you work with is correct structured and type safe.

# Firstly need to install pydantic `pip install pydantic`

from pydantic import BaseModel

class student(BaseModel):
    name:str

#In class we define name as a str but in new class we define
#will cannot be a different from the class which we defined
#It will return error

new_student={'name':12}

Student=student(**new_student)

print(Student)


