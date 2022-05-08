from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def root():
    return {"data" : "Welcome to the root"}

