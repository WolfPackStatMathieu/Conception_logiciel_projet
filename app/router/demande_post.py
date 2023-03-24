from fastapi import APIRouter, Body, Depends, Response, status
from pydantic import BaseModel, ValidationError, validator
import datetime as dt
from typing import Optional
from sqlalchemy.orm import Session
from app.dao.database import get_db
from app.dao import db_demande
from app.dao.schema import DemandeBase, DemandeDisplay
from app.custom_log import log

router = APIRouter(
    prefix='/demande',
    tags=['demande']
)



# Create Demande
@router.post('/',
             status_code=status.HTTP_200_OK,
            #  response_model= DemandeDisplay, # pour enlever le password de la reponse
             summary='crée une demande d\'envoi de mail avec hotmail.com',
             description="la demande d\'envoi est créée avec la date d\'envoi par défaut égale au moment de la requete. Il faut utiliser @hotmail.com",
             response_description='l\'identifiant de la demande')
def create_demande(request: DemandeBase , db: Session = Depends(get_db)):
    log("MyAPI", f"Call to create demande")
    return db_demande.create_demande(db, request)



#Update Demande
@router.post('{id}/update')
def update_demande(id: int, request: DemandeBase, db: Session= Depends(get_db)):
    log("MyAPI", f"Call to update demande {id}")
    return db_demande.update_demande(db, id, request)


