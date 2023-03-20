from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.route("/demandes")
async def demandes_route():
    """retourne toutes les demandes

    Returns
    -------
    JSON
        JSON avec toutes les demandes dedans
    """
    # TODO faire la requete dans la BDD qui renvoie
    # toutes les demandes
    return JSONResponse(content={"message": "Hello, world"})

@router.route("/demande/{demande_id}")
async def demande_by_id_route():
    """retourne la demande dont l'id est fourni

    Returns
    -------
    JSON
        JSON de la demande dont l'id est fourni en parametre
    """
    # TODO faire la requete dans la BDD qui renvoie
    # la demande de l'id fourni

    cursor = db_conn.cursor()
    cursor.execute("SELECT * FROM demandes")
    demandes = cursor.fetchall()
    return demandes
    # return JSONResponse(content={"message": "This is another example."})