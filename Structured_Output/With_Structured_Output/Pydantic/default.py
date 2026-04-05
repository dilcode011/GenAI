from pydantic import BaseModel

class Student(BaseModel):
    name:str='dilpreet'

new_student={}

student=Student(**new_student)
print(student.name)