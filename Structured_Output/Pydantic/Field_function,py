from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    name:str='dilpreet'
    age:Optional[int]=None
    email:EmailStr
    cgpa:float=Field(gt=0 , lt=10,default=6,description='A decimal value representing the cgpa of the student') 
    #if we are defining default value then we dont need to define value in new_student 


new_student={'age':21,'email':'abc@gmail.com','cgpa':5}

student=Student(**new_student) #pydantic value
print(student)



#Dict format 
student_dict=Dict(student)
print(student_dict['age'])


#json --> convert file into json
student_json=student.model_dump_json()