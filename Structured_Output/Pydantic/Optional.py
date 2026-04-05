from pydantic import BaseModel
from typing import Optional

class Student(BaseModel):
    name:str='dilpreet'
    age:Optional[int]=None

new_student={'age':21}

student=Student(**new_student)
print(student)