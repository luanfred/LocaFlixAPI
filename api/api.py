from fastapi import APIRouter
from api.endpoints import movie

api_router = APIRouter()

api_router.include_router(movie.router, prefix="/filmes", tags=["movies"])

