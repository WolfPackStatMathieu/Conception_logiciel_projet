from fastapi import FastAPI
from fastapi import APIRouter, status, Response


router = APIRouter(prefix='/demande', tags=['demande'])


@router.get(
    '/all',
    tags=['all'],
    summary='récupère toutes les demandes',
    description='This api call fetches all demandes',
    response_description='la liste de toutes les demandes')
def get_all_demande():
    """
    Récupère toutes les demandes
    """
    return {'message': 'toutes les demandes'}


@router.get('/{id}',
         status_code=status.HTTP_200_OK,
         tags=['id'],
         summary='trouve une demande par son id',
         description='This api call find a demande by its unique id',
         response_description='la demande dont l\'id a été fourni en paramètre')
def get_demande(id: int, response: Response):
    """Récupère une demande par son id

    - **id** mandatory path parameter

    """
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Demande {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message': f'Demande with id {id}'}

