from typing import Optional
from fastapi import FastAPI,Response,status,HTTPException
from pydantic import BaseModel
#from fastapi import Body
from fastapi.params import Body
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title:str
    content:str
    publish: bool=True
    rateing: Optional[int]

my_post = [
        {"title":"title of post","content":"contentof post1","id":1},
        {"title":"title2","content":"contentof post22","id":2}
    ]

def find_post(id):
    for p in my_post:
        if p['id'] == id:
            return p
        
def find_index_post(id):
    for i , p in enumerate(my_post):
        if p ["id"] == id:
            return i

@app.get("/")
def root():
    return{"message":"Filip 1312 "}          #sam ga prevede u JSON  ctrlshift arrow

@app.get("/posts")
def get_posts():
    return {"data":my_post} #sam ga prevede u json

@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    post_dict = post.model_dump()
    post_dict["id"] = randrange(0,1000)
    my_post.append(post_dict)
    return{"data":post_dict}

@app.get("/posts/{id}")
def get_post(id:int, response:Response):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='post not found')
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message":"post not found"}
    return post

@app.delete("post/{id}")
def delete_post(id:int):
    index = find_index_post(id)
    my_post.pop(index)

    return {"message":"post deleted"}