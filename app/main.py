from fastapi import FastAPI, APIRouter, status

app = FastAPI()
router = APIRouter()


@router.get('/')
def get_notes():
    return "return a list of note items"


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_note():
    return "create note item"


@router.patch('/{noteId}')
def update_note(noteId: str):
    return f"update note item with id {noteId}"


@router.get('/{noteId}')
def get_note(noteId: str):
    return f"get note item with id {noteId}"


@router.delete('/{noteId}')
def delete_note(noteId: str):
    return f"delete note item with id {noteId}"


app.include_router(router, tags=['Notes'], prefix='/api/notes')


@app.get("/api/healthchecker")
def root():
    return {"message": "Welcome to FastAPI with SQLAlchemy"}





# @app.on_event("startup")
# async def startup():


#     # Set up a background task that runs every 60 seconds
#     async def check_objects(background_tasks: BackgroundTasks):
#         while True:
#             # Get the current datetime
#             now = datetime.datetime.now()

#             # Perform checks on your Python objects here
#             # For example, you could query the database to find all objects that have an expiration date less than or equal to the current date
#             c = conn.cursor()
#             c.execute("SELECT * FROM mytable WHERE expiration_date <= ?", (now,))
#             expired_objects = c.fetchall()

#             # Do something with the expired objects, such as delete them from the database
#             for obj in expired_objects:
#                 # Delete the object
#                 c.execute("DELETE FROM mytable WHERE id = ?", (obj['id'],))
#                 conn.commit()

#             # Wait for 60 seconds before checking again
#             await asyncio.sleep(60)

#     # Start the background task
#     app.background_tasks.add_task(check_objects)

# @app.on_event("shutdown")
# async def shutdown():
#     # Close the database connection when the app shuts down
#     conn.close()
