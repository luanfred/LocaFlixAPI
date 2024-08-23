from typing import List
from fastapi import APIRouter, HTTPException, status, Response
from sqlalchemy.future import select
from models.movie_model import MovieModel
from schemas.movie_schema import MovieSchema
from core.deps import db_dependency

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=MovieSchema)
def create_movie(movie: MovieSchema, db: db_dependency):
    new_movie = MovieModel(
        title=movie.title,
        director=movie.director,
        year=movie.year
    )
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)

    return new_movie


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[MovieSchema])
def get_movies(db: db_dependency):
    query = select(MovieModel)
    result = db.execute(query)
    movies: List[MovieModel] = result.scalars().all()

    return movies
    

@router.get("/{movie_id}", status_code=status.HTTP_200_OK, response_model=MovieSchema)
def get_movie(movie_id: int, db: db_dependency):
    query = select(MovieModel).where(MovieModel.id == movie_id)
    result = db.execute(query)
    movie: MovieModel = result.scalar_one_or_none()

    if movie is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")

    return movie
    

@router.put("/{movie_id}", status_code=status.HTTP_202_ACCEPTED, response_model=MovieSchema)
def update_movie(movie_id: int, movie: MovieSchema, db: db_dependency):
    query = select(MovieModel).where(MovieModel.id == movie_id)
    result = db.execute(query)
    movie_to_update: MovieModel = result.scalar_one_or_none()

    if movie_to_update is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")

    movie_to_update.title = movie.title
    movie_to_update.director = movie.director
    movie_to_update.year = movie.year
    db.commit()
    db.refresh(movie_to_update)

    return movie_to_update


@router.delete("/{movie_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_movie(movie_id: int, db: db_dependency):
    query = select(MovieModel).where(MovieModel.id == movie_id)
    result = db.execute(query)
    movie_to_delete: MovieModel = result.scalar_one_or_none()
    if movie_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")

    db.delete(movie_to_delete)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
