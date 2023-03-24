
from fastapi import FastAPI, APIRouter, status, Response, BackgroundTasks
from app.router import demande_get
from app.router import demande_post
from app.dao import models
from app.dao.database import engine
from app.dao.database import get_db
from sqlalchemy.orm import Session
from fastapi_utils.session import FastAPISessionMaker
from fastapi_utils.tasks import repeat_every

#background task
import smtplib
import datetime as dt
import random
from app.custom_log import log

app = FastAPI()
app.include_router(demande_get.router)
app.include_router(demande_post.router)

models.Base.metadata.create_all(engine)


def send_email_to_be_sent(db: Session) -> None:
    """Pretend this function send emails to be sent"""


@app.on_event("startup")
@repeat_every(seconds=60 * 60)  # 1 hour
def send_email_to_be_sent_task() -> None:
    session = get_db()
    with session as db:
        send_email_to_be_sent(db)

# @app.on_event("startup")
# async def startup():


#     # Set up a background task that runs every 60 seconds
    # async def check_objects(background_tasks: BackgroundTasks):
        # while True:
        #     session = get_db()

#             # Get the current datetime
            # now = dt.datetime.now()

#             # Perform checks on your Python objects here
#             # For example, you could query the database to find all objects that have an expiration date less than or equal to the current date
#             c = conn.cursor()
#             c.execute("SELECT * FROM mytable WHERE expiration_date <= ?", (now,))
#             expired_objects = c.fetchall()
            # email_a_envoyer = demande_get.get_all_demandes(session)
            # log(tag="email à envoyer", str(email_a_envoyer))

    #         with smtplib.SMTP("smtp-mail.outlook.com") as connection:
    #         starttls()
    #         connection.login(user= my_email, password=password)
    #         connection.sendmail(
    #             from_addr=my_email,
    #             to_addrs="mathieu993@hotmail.com",
    #             msg=f"Subject:Quote of Thursday\n\n{quote}"
    #         )
    # if day_of_week == 3:
    #     sendmail(my_email, password, quote)
#             # Do something with the expired objects, such as delete them from the database
#             for obj in expired_objects:
#                 # Delete the object
#                 c.execute("DELETE FROM mytable WHERE id = ?", (obj['id'],))
#                 conn.commit()

#             # Wait for 60 seconds before checking again
#             await asyncio.sleep(60)

#     # Start the background task
    # app.background_tasks.add_task(check_objects)

# @app.on_event("shutdown")
# async def shutdown():
#     # Close the database connection when the app shuts down
    # conn.close()
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)