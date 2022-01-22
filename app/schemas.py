from pydantic import BaseModel, EmailStr


class CourseBase(BaseModel):
    '''
    Schema to validate the user's input
    '''
    course_id: int
    name: str
    available: bool = True
    offered_days: str
    offered_time: str


class Course(BaseModel):
    '''
    Schema to validate the data that will be sent to the user
    '''
    course_id: int
    name: str
    available: bool = True
    offered_days: str
    offered_time: str

    class Config:
        orm_mode = True


class CourseOut(BaseModel):
    '''
    Schema to validate the data that will be sent to the user
    '''
    course_id: int
    name: str

    class Config:
        orm_mode = True


class StudentCreate(BaseModel):
    '''
    Schema to validate the user's input
    '''
    student_id = int
    name: str
    email: EmailStr


class StudentOut(BaseModel):
    '''
    Schema to validate the data that will be sent to the user
    '''
    student_id: int
    name: str
    email: EmailStr
    courses_currently_enrolled: int
    courses_currently_taking: CourseOut

    class Config:
        orm_mode = True
