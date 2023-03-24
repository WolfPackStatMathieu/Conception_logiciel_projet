from fastapi import APIRouter
from pydantic import BaseModel, ValidationError, validator
import datetime as dt
from typing import Optional

router = APIRouter(
    prefix='/demande',
    tags=['demande']
)
class DemandeModel(BaseModel):
    destinataire: str
    expediteur: str
    password: str
    sujet: str
    message: str
    mois: int
    jour: int
    heure: int
    minutes: int
    id: int

    @validator('destinataire')
    def destinataire_must_contain_arobase(cls, v):
        if '@' not in v:
            raise ValueError('must contain an arobase @')
        return v.title()

    @validator('expediteur')
    def expediteur_must_contain_arobase(cls, v):
        if '@' not in v:
            raise ValueError('must contain an arobase @')
        return v.title()

    @validator('mois')
    def mois_must_be_from_1_to_12(cls, v):
        if v<=0 or v>12:
            raise ValueError('must be between 1 and 12')
        return v

    @validator('jour')
    def jour_must_be_from_1_to_31(cls, v):
        if v<=0 or v>=32:
            raise ValueError('must be between 1 and 31')
        return v

    @validator('heure')
    def heure_must_be_from_0_to_23(cls, v):
        if v<0 or v>24:
            raise ValueError('must be between 0 and 23')
        return v

    @validator('minutes')
    def minutes_must_be_from_0_to_59(cls, v):
        if v<0 or v>59:
            raise ValueError('must be between 0 and 59')
        return v

@router.post('/',
             summary='crée une demande d\'envoi de mail')
def create_demande(demande: DemandeModel):
    return {'data': demande.minutes}