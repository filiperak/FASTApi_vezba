from fastapi import Body, FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"data":"data"}

@app.get("/posts")
def get_posts():
    return {"data":"postdata"}

@app.post("/createpost")
def create_posts(payload:dict = Body(...)):
    print(payload)
    return {"new_post":f"title: {payload['title']} , content: {payload['content']}"}
    