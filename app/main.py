from fastapi import FastAPI
from .routers import courses, students

# Create a FastAPI instance
app = FastAPI()

# Include the routers from the 'courses' and 'students' submodules. It will  create a path operation for each path operation that was declared in the APIRouter
app.include_router(courses.router)
app.include_router(students.router)


@app.get('/')
def root():
    return {"Message": "Welcome to the Student Enrollment Portal. Head to '/courses' to see courses, or '/students' to see students"}
