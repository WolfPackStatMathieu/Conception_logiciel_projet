from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.route("/demandes")
async def demandes_route():
    # TODO faire la requete dans la BDD qui renvoie
    # toutes les demandes
    return JSONResponse(content={"message": "Hello, world"})

@router.route("/demande/{demande_id}")
async def demande_by_id_route():
    # TODO faire la requete dans la BDD qui renvoie
    # la demande de l'id fourni
    return JSONResponse(content={"message": "This is another example."})