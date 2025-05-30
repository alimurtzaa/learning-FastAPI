from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get('/')
def index():
    return {'data':{'name':'murtza ali'}}

@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blogs'}

@app.get('/blog')
def show(limit=10, published: bool=True, sort:Optional[str]=None):
    if published:
        return {'data':f'{limit} published blogs from the list'}
    else:
        return {'data':f'{limit} blogs from the list'}
        
@app.get('/blog/{id}')
def show(id: int):
    return {'data':id}

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def create_blog(blog: Blog):  # here this blog = request body
    return {'data': f'blog is created with title {blog.title}'}

@app.get('/about')
def about():
    return {'data':'about page'}



# To run at server at different port

# This code only runs when the file is executed directly, not when it's imported.
# if __name__ == "__main__":
#     uvicorn.run(app, host='127.0.0.1', port=9000)