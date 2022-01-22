
from sqlalchemy import Column, Integer, Boolean, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

# Create a table in postgres with the following attributes
# Create SQLAlchemy models by using the Base class


class Course(Base):
    '''
    A class to create a SQLAlchemy model for Course
    It creates a table in PostgreSQL with the following attributes

    Attributes
    ----------
    __tablename__ : str
        Name of the table
    course_id: int
        The id of the course
    name: int
        The name of the course
    available: bool
        The availablity of the course
    offered_days: str
        Days in which the course is offered
    offered_time: str
        Time in which the course is offered
    '''
    __tablename__ = 'courses'
    course_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    available = Column(Boolean, server_default='TRUE', nullable=False)
    offered_days = Column(String, nullable=True)
    offered_time = Column(String, nullable=True)


class Student(Base):
    '''
    A class to create a SQLAlchemy model for Student
    It creates a table in PostgreSQL with the following attributes

    Attributes
    ----------
    __tablename__ : str
        Name of the table
    student_id: int
        ID of the student
    name: str
        Name of the student
    email: str
        Email of the student
    course_currently_enrolled: int
        ID of the courses the student is currently enrolled in
    courses_currently_taking: json
        JSON object of the information of the courses that the user is currently enrolled in
    '''
    __tablename__ = 'students'
    student_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    courses_currently_enrolled = Column(Integer, ForeignKey(
        "courses.course_id", ondelete="CASCADE"), nullable=True)
    courses_currently_taking = relationship("Course")
