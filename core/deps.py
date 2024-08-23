from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session
from core.database import SessionLocal

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

db_dependency = Annotated[Session, Depends(get_session)]