from .. import schemas
from ..database import get_db
from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from ..repository import blog
from typing import Annotated
from ..oauth2 import get_current_user

router = APIRouter(
    prefix="/blog",
    tags=["Blog"]
)

@router.get('/', response_model=List[schemas.ShowBlog])
def all_blogs(db: Annotated[Session, Depends(get_db)], current_user: Annotated[schemas.User, Depends(get_current_user)]):
    return blog.get_all(db)

@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id: int, db: Annotated[Session, Depends(get_db)], current_user: Annotated[schemas.User, Depends(get_current_user)]):
    return blog.sohw(id, db)

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Annotated[Session, Depends(get_db)], current_user: Annotated[schemas.User, Depends(get_current_user)]):
    return blog.create(request, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: schemas.Blog, db: Annotated[Session, Depends(get_db)], current_user: Annotated[schemas.User, Depends(get_current_user)]):
    return blog.update(id, request, db)

@router.delete('/{id}', status_code=status.HTTP_200_OK)
def destroy(id: int, db: Annotated[Session, Depends(get_db)], current_user: Annotated[schemas.User, Depends(get_current_user)]):
    return blog.destroy(id, db)