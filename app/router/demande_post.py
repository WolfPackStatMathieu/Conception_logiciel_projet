from fastapi import APIRouter, Body, Depends
from pydantic import BaseModel, ValidationError, validator
import datetime as dt
from typing import Optional
from sqlalchemy.orm import Session
from app.dao.database import get_db
from app.dao import db_demande
from app.dao.schema import DemandeBase, DemandeDisplay

router = APIRouter(
    prefix='/demande',
    tags=['demande']
)



# Create Demande
@router.post('/',
            #  response_model= DemandeDisplay, # pour enlever le password de la reponse
             summary='crée une demande d\'envoi de mail avec hotmail.com',
             description="la demande d\'envoi est créée avec la date d\'envoi par défaut égale au moment de la requete. Il faut utiliser @hotmail.com")
def create_demande(request: DemandeBase , db: Session = Depends(get_db)):
    return db_demande.create_demande(db, request)


# Read Demande

#Update Demande

# Delete Demande


