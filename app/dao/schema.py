from pydantic import BaseModel, validator, ValidationError
from fastapi import Body
import datetime as dt
from typing import Optional


now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
hour_of_now = now.hour
minutes_of_now = now.minute


class DemandeBase(BaseModel):
    # id = int
    destinataire: str = Body('mathieu993@hotmail.com',
                             min_length=1,
                             regex= '^[A-Za-z0-9]*@hotmail.com') #email
    expediteur: str= Body('mathieu993@hotmail.com',
                            min_length=1,
                            regex= '^[A-Za-z0-9]*@hotmail.com') #email
    password: str
    sujet: str
    message: str
    mois: int = month
    jour: int = day
    heure: int =hour_of_now
    minutes: int =minutes_of_now
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


class DemandeDisplay(BaseModel):
    #on enlève le password du retour
    # id = int
    destinataire: str
    expediteur: str
    sujet: str
    message: str
    mois: int
    jour: int
    heure: int
    minutes: int
    class Config():
        orm_mode = True
