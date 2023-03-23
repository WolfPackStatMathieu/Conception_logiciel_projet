
from fastapi import FastAPI
from enum import Enum

app = FastAPI()

@app.get('/hello')
def index():
    return {'message': 'Hello world!'}

@app.get('/demande/all')
def get_all_demande():
    return {'message': 'toutes les demandes'}


class DemandeType(str, Enum):
    texte= 'texte'
    image= 'image'
    fichier= 'fichier'

@app.get('/demande/type/{type}')
def get_demande_type(type: DemandeType):
    return {'message': f'Demande type {type}'}

@app.get('/demande/{id}')
def get_demande(id: int):
    return {'message': f'Demande with id {id}'}




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
