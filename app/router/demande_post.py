from fastapi import APIRouter

router = APIRouter(
    prefix='/demande',
    tags=['demande']
)

@router.post('/')
def create_post():
    pass