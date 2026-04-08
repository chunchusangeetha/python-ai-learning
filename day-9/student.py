from fastapi import FastAPI
import json
from pydantic import BaseModel

class Student(BaseModel):
    name:str
    marks:int

app = FastAPI()

FILE  = "student.json"

@app.get('/')
def home():
    return{
        "status": "success",
        "message":"created home page for students"
    }

@app.get('/students')
def get_students():
    with open(FILE, "r") as f:
        data = json.load(f)
       
    return {
        "status": "success",
        "data": data
    }

@app.post('/students')
def create_students(student:Student):
    with open(FILE,"r") as f:
        students = json.load(f)
        students.append(student.dict())
    with open(FILE, "w") as f:
        json.dump(students, f, indent=2)
    return {
        "status":"success",
        "message":"created student successfully",
        "data":students

    } 

@app.put('/students/{name}')
def update_students(name:str,updated:Student):
    with open(FILE, "r") as f:
        students = json.load(f)

    for s in students:
        if s["name"].lower() == name.lower():
            s["marks"] = updated.marks
            with open(FILE ,"w") as f:
                json.dump(students,f)
            return {
                "status":"success",
                "message":"updated student successfully",
                "data":s
            }
    return {
        "status":"error",
        "message":"student not found"
    }              

@app.delete('/students/{name}')
def delete_students(name:str):
    with open(FILE, "r") as f:
        students = json.load(f)
        
    for s in students:
        if s["name"] == name:
            students.remove(s)
            with open(FILE, "w") as f:
                json.dump(students, f, indent=2)
            return {
                "status":"success",
                "data":students,
                "message":"deleted student successfully",
            } 
    return {
        "status":"error",
        "message":"student not found"
    }     