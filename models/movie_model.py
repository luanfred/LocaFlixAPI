from sqlalchemy import Column, Integer, String

from core.database import Base

class MovieModel(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    title = Column(String(100))
    director = Column(String(100))
    year = Column(Integer)
