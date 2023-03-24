from fastapi import APIRouter, Body
from pydantic import BaseModel, ValidationError, validator
import datetime as dt
from typing import Optional, Set
import datetime as dt

router = APIRouter(
    prefix='/demande',
    tags=['demande']
)

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
hour_of_now = now.hour
minutes_of_now = now.minute
class DemandeModel(BaseModel):

    destinataire: str = Body(...,
                             min_length=1,
                             regex= '^[A-Za-z0-9]*@[A-Za-z0-9]*$') #email
    expediteur: str= Body(...,
                            min_length=1,
                            regex= '^[A-Za-z0-9]*@[A-Za-z0-9]*$') #email
    password: str
    sujet: str = Body(...,
                      min_length=1,
                      max_length=120)
    message: str = Body(...,
                        min_length=2,
                        max_length=20000)
    mois: int = month
    jour: int = day
    heure: int =hour_of_now
    minutes: int =minutes_of_now
    id: int
    est_envoye : Optional[bool]=False

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
             summary='crée une demande d\'envoi de mail',
             description="la demande d\'envoi est créée avec la date d\'envoi par défaut égale au moment de la requete")
def create_demande(demande: DemandeModel, id: int):
    return {
        'id': id,
        'data': demande
        }