from pydantic import BaseModel,EmailStr
from typing import Optional

class Student(BaseModel):
    name:str='dilpreet'
    age:Optional[int]=None
    email:EmailStr

new_student={'age':21,'email':'abc'} #return error inspite it does not include @gmail.com
new_student={'age':21,'email':'abc@gmail.com'} #does not return error aas it include @gmail.com

student=Student(**new_student)
print(student)
