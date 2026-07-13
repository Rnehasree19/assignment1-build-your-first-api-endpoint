from fastapi import FastAPI

app = FastAPI()

@app.get("/greeting")
def greeting():
    return {"greeting": "hello"}

@app.get("/name")
def name():
    return {"name": "Neha"}