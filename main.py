from fastapi import FastAPI
from api.api import api_router
from models import movie_model
from core.database import engine

movie_model.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Locadora de Filmes",
    description="API para locadora de filmes",
)
app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, log_level="info")
