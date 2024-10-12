from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return{"message":"Filip 1312 "}          #sam ga prevede u JSON

