from typing import Optional
from fastapi import Body, FastAPI, Response,status
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title:str
    content:str
    published:bool = True
    rating: Optional[float] = None

my_posts = [
    {"title":"title of post 1","content":"content of post1","id":1},
    {"title":"title of post 2","content":"content of post2","id":2}
    ]

def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p

@app.get("/")
def root():
    return {"data":"data"}

@app.get("/posts")
def get_posts():
    return {"data":my_posts}

# @app.post("/createpost")
# def create_posts(payload:dict = Body(...)):
#     print(payload)
#     return {"new_post":f"title: {payload['title']} , content: {payload['content']}"}

# @app.post("/createpost")
# def create_posts(new_post:Post):
#     print(new_post)
#     print(new_post.dict())
#     return {"new_post":new_post}


@app.post("/posts")
def create_posts(new_post:Post):
    #print(new_post)
    #print(new_post.model_dump())
    post_dict = new_post.model_dump()
    post_dict['id'] = randrange(0,1000)
    my_posts.append(post_dict)

    return {"new_post":new_post}

@app.get("/posts/{id}")
def get_post(id:int,response:Response):
    post = find_post(id)
    if not post:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"messsage":"post not found"}

    return {"post_detail":post}

@app.delete("posts/{id}")
def delete_post(id):
    pass