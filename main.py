from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title:str
    content:str
    published:bool = True
    rating: Optional[float] = None

@app.get("/")
def root():
    return {"data":"data"}

@app.get("/posts")
def get_posts():
    return {"data":"postdata"}

# @app.post("/createpost")
# def create_posts(payload:dict = Body(...)):
#     print(payload)
#     return {"new_post":f"title: {payload['title']} , content: {payload['content']}"}

@app.post("/createpost")
def create_posts(new_post:Post):
    print(new_post.published)
    return {"new_post":new_post}
