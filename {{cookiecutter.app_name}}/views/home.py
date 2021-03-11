import fastapi
from fastapi_chameleon import template

router = fastapi.APIRouter()


@router.get('/')
@template('home/index.pt')
def index():
    return {}
