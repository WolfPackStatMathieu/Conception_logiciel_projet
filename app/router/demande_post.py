from fastapi import APIRouter
from pydantic import BaseModel
import datetime as dt
from typing import Optional

router = APIRouter(
    prefix='/demande',
    tags=['demande']
)
class DemandeModel(BaseModel):
    destinataire: str
    expediteur: str
    sujet: str
    message: str
    mois: int
    jour: int
    heure: int
    minutes: int
    id: int



@router.post('/',
             summary='crée une demande d\'envoi de mail')
def create_demande(demande: DemandeModel):
    return {'data': demande}