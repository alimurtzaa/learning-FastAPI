from .. import schemas
from ..database import get_db
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List 
from ..repository import user

router = APIRouter(
    prefix="/user",
    tags=["User"]
)

@router.get('/', status_code=200, response_model=List[schemas.ShowUser])
def all_users(db: Session = Depends(get_db)):
    return user.all_user(db)

@router.get('/{id}', status_code=200, response_model=schemas.ShowUser)
def show_user(id: int, db: Session = Depends(get_db)):
    return user.show(id, db)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)