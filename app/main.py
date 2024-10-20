from typing import Optional
from fastapi import Body, FastAPI, Response,status,HTTPException
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

def find_post_index(id):
    for i,post in enumerate(my_posts):
        if post["id"] == id:
            return i

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


@app.post("/posts",status_code=status.HTTP_201_CREATED)
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
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {"messsage":"post not found"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="post not found")

    return {"post_details":post}



@app.delete("/posts/{id}")
def delete_post(id:int):
    index = find_post_index(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="post not found")
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(updated_post:Post,id:int):
    index = find_post_index(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="post not found")
    
    post_dict = updated_post.model_dump()
    post_dict["id"] = id
    my_posts[index] = post_dict
    print(updated_post)
    return{"message":f"post {id} updated"}