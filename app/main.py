
from fastapi import FastAPI, status, Response
from enum import Enum

app = FastAPI()



@app.get(
    '/demande/all',
    tags=['demande', 'all'],
    summary='récupère toutes les demandes',
    description='This api call fetches all demandes',
    response_description='la liste de toutes les demandes')
def get_all_demande():
    """
    Récupère toutes les demandes
    """
    return {'message': 'toutes les demandes'}


@app.get('/demande/{id}',
         status_code=status.HTTP_200_OK,
         tags=['demande', 'id'],
         summary='trouve une demande par son id',
         description='This api call find a demande by its unique id',
         response_description='la demande dont l\'id a été fourni en paramètre')
def get_demande(id: int, response: Response):
    """Récupère une demande par son id

    - **id** mandatory path parameter

    """
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Demande {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
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
