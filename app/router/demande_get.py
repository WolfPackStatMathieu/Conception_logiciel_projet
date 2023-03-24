from fastapi import FastAPI, Depends
from fastapi import APIRouter, status, Response
from typing import List
from app.dao.schema import DemandeBase, DemandeDisplay
from sqlalchemy.orm.session import Session
from app.dao.database import get_db
from app.dao import db_demande
from app.custom_log import log


router = APIRouter(prefix='/demande', tags=['demande'])

# Read all demandes
@router.get(
    '/all',
    status_code=status.HTTP_200_OK,
    tags=['all'],
    summary='récupère toutes les demandes',
    description='This api call fetches all demandes',
    response_description='la liste de toutes les demandes'
    # ,response_model=List[DemandeBase]
    )
def get_all_demandes(db: Session = Depends(get_db)):
    """
    Récupère toutes les demandes
    """
    log("MyAPI", "Call to get all demandes")
    return db_demande.get_all_demandes(db)


# Get Demandes to send
@router.get('/to_send')
def get_demande_to_send(db: Session = Depends(get_db)):
    log("MyAPI", f"Call to get_demande_to_send")
    return db_demande.get_demande_to_send(db)

#check and send email
@router.get('/check_and_send')
def check_and_send(db: Session = Depends(get_db)):
    #QUery database for items with est_envoye == False
    demandes = db_demande.get_demande_to_send(db)
    # for demande in demandes:
    #     if demande.



# Read one Demande
@router.get('/{id}',
         status_code=status.HTTP_200_OK,
         tags=['id'],
         summary='trouve une demande par son id',
         description='This api call find a demande by its unique id',
         response_description='la demande dont l\'id a été fourni en paramètre'
        #  , response_model=List[DemandeDisplay]
        )
def get_demande(id: int, db: Session = Depends(get_db)):
    """Récupère une demande par son id

    - **id** mandatory path parameter

    """
    log("MyAPI", f"Call to get demande {id}")
    return db_demande.get_demande(db, id)

# Delete Demande
@router.get('/delete/{id}')
def delete(id: int, db: Session = Depends(get_db)):
    log("MyAPI", f"Call to delete demande {id}")
    return db_demande.delete_demande(db, id)
