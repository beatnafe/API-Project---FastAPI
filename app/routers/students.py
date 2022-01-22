from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas
from ..database import get_db


router = APIRouter()


@router.get('/student', response_model=List[schemas.StudentOut])
def get_all_students(db: Session = Depends(get_db)):
    '''
    Gets all students

    Parameters
    ----------
    db : Session
        The database session that depends on ..database.get_db
    '''
    students = db.query(models.Student).all()
    return students


@router.get('/student/{id}', response_model=schemas.StudentOut)
def get_student(id: int, db: Session = Depends(get_db)):
    '''
    Gets a specific student when a user provides a student-id

    Parameters
    ----------
    id : int
        The id of the student the user is searching for
    db : Session
        The database session that depends on ..database.get_db

    Raises
    ------
    404 - Not Found
        If a student with the specified student-id is not found
    '''
    student = db.query(models.Student).filter(
        models.Student.student_id == id).first()
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Student with Student-ID:{id} does not exist")
    return student


@router.post('/student', response_model=schemas.StudentOut, status_code=status.HTTP_201_CREATED)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    '''
    Create a student account

    Parameters
    ----------
    student: schemas.StudentCreate
        Information of the student account that is going to be created. 
        It follows the schema as stated in schemas.StudentCreate
    db : Session
        The database session that depends on ..database.get_db

    Raises
    ------
    201 - Created
        Once student account has been created
    '''
    new_student = models.Student(**student.dict())
    db.add(new_student)
    db.commit()
    db.refrest(new_student)
    return new_student


@router.delete('/student/{id}')
def remove_student(id: int, db: Session = Depends(get_db)):
    '''
    Removes a specific student when a user provides a student-ID

    Parameters
    ----------
    id : int
        The id of the student the user is trying to remove
    db : Session
        The database session that depends on ..database.get_db

    Raises
    ------
    204 - No Content
        If the student with the specified student-id is removed
    404 - Not Found
        If a student with the specified student-id is not found
    '''
    student_query = db.query(models.Student).filter(
        models.Student.student_id == id)
    student = student_query.first()
    if student == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Student with Student-ID:{id} does not exist")
    student_query.delete(synchronize_session=False)
    db.commit
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put('/student/{id}', response_model=schemas.StudentOut)
def update_student(id: int, updated_student: schemas.StudentCreate, db: Session = Depends(get_db)):
    '''
    Updates a student account when a user provides a student-ID

    Parameters
    ----------
    id : int
        The id of the student the user is trying to update
    updated_student: schemas.StudentCreate
        Updated information of the student
        It follows the schema as stated in schemas.StudentCreate
    db : Session
        The database session that depends on ..database.get_db

    Raises
    ------
    404 - Not Found
        If no student with the specified student-id is not found
    '''
    student_query = db.query(models.Student).filter(
        models.Student.student_id == id)
    student = student_query.first()
    if student == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Student with Student-ID:{id} does not exist")
    student_query.update(updated_student.dict(), synchronize_session=False)
    db.commit
    return student_query.first()
