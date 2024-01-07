from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, Naveen!"}

@app.get("/about")
def read_about():
    return {"message": "About, Naveen!"}

@app.get("/services")
def read_services():
    return {"message": "Services!"}
