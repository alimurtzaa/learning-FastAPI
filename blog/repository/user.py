from .. import schemas, models
from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from ..hashing import Hash 

def all_user(db: Session):
    users = db.query(models.User).all()
    if users:
        return users
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No users')

def show(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No user with id {id}')
    return user

def create(request:schemas.User, db: Session):
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user