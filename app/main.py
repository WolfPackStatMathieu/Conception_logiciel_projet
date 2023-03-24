
from fastapi import FastAPI, APIRouter, status, Response, BackgroundTasks
from app.router import demande_get
from app.router import demande_post
from app.dao import models
from app.dao.database import engine
from app.dao.database import get_db
from sqlalchemy.orm import Session
from fastapi_utils.session import FastAPISessionMaker
from fastapi_utils.tasks import repeat_every
from apscheduler.schedulers.background import BackgroundScheduler
from app.controller import send_email


#background task
import smtplib
import datetime as dt
import random
from app.custom_log import log

app = FastAPI()

scheduler = BackgroundScheduler()

app.include_router(demande_get.router)
app.include_router(demande_post.router)

models.Base.metadata.create_all(engine)


# @app.on_event("startup")
# def start_scheduler():
#     scheduler.add_job(
#         func=check_and_send,
#         trigger="interval",
#         seconds= 60
#     ) # run every minute
#     scheduler.start()

# @app.post('/send_emails')
# async def trigger_send_emails(background_tasks: BackgroundTasks):
#     background_tasks.add_task(check_and_send)
#     return {"message": "Emails will be sent soon."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)