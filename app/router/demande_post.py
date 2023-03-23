from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter(
    prefix='/demande',
    tags=['demande']
)
class DemandeModel(BaseModel):
    pass


@router.post('/',
             summary='crée une demande d\'envoi de mail')
def create_demande(demande: DemandeModel):
    return "ok"