from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {
        "status": "success",
        "message": "This is my first API"
    }

@app.get('/students')
def students():
    return {
        "status": "success",
        "data": "This is student route"
    }

@app.get('/contacts')       
def contact():
    return {
        "status": "success",
        "data": "This is contact page route"
    }