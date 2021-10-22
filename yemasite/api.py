from ninja import NinjaAPI
from api.api import api as api_router


api = NinjaAPI()
api.add_router('/', api_router)
