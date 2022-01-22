from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas
from ..database import get_db

# Create a Path operator
router = APIRouter()


@router.get('/course/{id}', response_model=schemas.Course)
def get_course(id: int, db: Session = Depends(get_db)):
    '''
    Gets a specific course when a user provides a course-ID

    Parameters
    ----------
    id : int
        The id of the course the user is searching for
    db : Session
        The database session that depends on ..database.get_db

    Raises
    ------
    404 - Not Found
        If a course with the specified course-id is not found
    '''
    course = db.query(models.Course).filter(
        models.Course.course_id == id).first()
    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Course with id: {id} was not found")
    return course


@router.get('/course', response_model=List[schemas.Course])
def get_all_courses(db: Session = Depends(get_db)):
    '''
    Gets all courses

    Parameters
    ----------
    db : Session
        The database session that depends on ..database.get_db
    '''
    courses = db.query(models.Course).all()
    return courses


@router.post('/course', status_code=status.HTTP_201_CREATED, response_model=schemas.Course)
def create_course(course: schemas.CourseBase, db: Session = Depends(get_db)):
    '''
    Create a course

    Parameters
    ----------
    course : schemas.CourseBase
        Information of the course that is going to be created. 
        It follows the schema as stated in schemas.CourseBase
    db : Session
        The database session that depends on ..database.get_db

    Raises
    ------
    201 - Created
        Once course has been created
    '''
    new_course = models.Course(**course.dict())
    db.add(new_course)
    db.commit()
    db.refresh(new_course)


@router.delete('/course/{id}', status_code=status.HTTP_204_NO_CONTENT)
def remove_course(id: int, db: Session = Depends(get_db)):
    '''
    Removes a specific course when a user provides a course-ID

    Parameters
    ----------
    id : int
        The id of the course the user is trying to remove
    db : Session
        The database session that depends on ..database.get_db

    Raises
    ------
    204 - No Content
        If the course with the specified course-id is removed
    404 - Not Found
        If a course with the specified course-id is not found
    '''
    course_query = db.query(models.Course).filter(
        models.Course.course_id == id)
    course = course_query.first()
    if course == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Course with ID:{id} does not exist")
    course_query.delete(synchronize_session=False)
    db.commit
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put('/course/{id}', response_model=schemas.Course)
def update_course(id: int, updated_course: schemas.CourseBase, db: Session = Depends(get_db)):
    '''
    Updates a specific course when a user provides a course-ID

    Parameters
    ----------
    id : int
        The id of the course the user is trying to update
    updated_course: schemas.CourseBase
        Updated information of the course
        It follows the schema as stated in schemas.CourseBase
    db : Session
        The database session that depends on ..database.get_db

    Raises
    ------
    404 - Not Found
        If no course with the specified course-id is not found
    '''
    course_query = db.query(models.Course).filter(
        models.Course.course_id == id)
    course = course_query.first()
    if course == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"post with ID:{id} does not exist")
    course_query.update(updated_course.dict(), synchronize_session=False)
    db.commit
    return course_query.first()
