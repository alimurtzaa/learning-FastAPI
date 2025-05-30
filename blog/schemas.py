from pydantic import BaseModel, Field
from typing import Annotated, List


class Blog(BaseModel):
    title: str
    body: str

class User(BaseModel):
    name: Annotated[str, Field(...,description="Enter name")]
    email: Annotated[str, Field(...,description="Enter email")]
    password: Annotated[str, Field(...,description="Enter password")]

class ShowUser(BaseModel):
    id: int
    name: str
    email: str
    blogs: List[Blog]

    class Config:
        from_attributes = True

class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser

    class Config:   # db se Sqlalchemy model return hota hai, usse pydantic handle kr sake response model me isliye
        from_attributes = True

class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None