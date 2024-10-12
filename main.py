from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
#from fastapi import Body
from fastapi.params import Body

app = FastAPI()

class Post(BaseModel):
    title:str
    content:str
    publish: bool=True
    rateing: Optional[int]


@app.get("/")
def root():
    return{"message":"Filip 1312 "}          #sam ga prevede u JSON  ctrlshift arrow

@app.get("/posts")
def get_posts():
    return {"data":"this is your post"}

@app.post("/createpost")
def create_post(post: Post):
    print(post.publish)
    print(post.model_dump())
    return{"post":post}


