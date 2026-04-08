import json
from fastapi import FastAPI,status,HTTPException,Query
from pydantic import BaseModel,EmailStr,PastDate,Field  
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
FILE = 'user.json'

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    user_name:str = Field(..., min_length=3, max_length=30)
    user_email:EmailStr 
    user_dob:PastDate 

class UserResponse(BaseModel):
    status: str
    data: list[User]

@app.get('/')
def home():
    return {
        "status":"success",
        "message":"this the home page of user"
    }

def read_user():
    with open(FILE,'r') as f:
        try:
            return json.load(f)
        except:
            return [] 

def write_user(users):
    with open(FILE,"w") as f:
        json.dump(users,f,indent=4)

# @app.get('/users')
# def get_user():
#     user = read_user()
#     return {
#         "status":"success",
#         "data":user
#     }

@app.get("/users", response_model=UserResponse)
def get_users(
    name: str | None = Query(default=None),
    email: str | None = Query(default=None),
    limit: int = Query(default=10, ge=1),
    skip: int = Query(default=0, ge=0),
    sort: str | None = Query(default=None)
):
    users = read_user()

    if name is not None and name.strip() != "":
        users = [
            user for user in users
            if name.lower() in user["user_name"].lower()
        ]

    if email:
        users = [
            user for user in users
            if email.lower() in user["user_email"].lower()
        ]

    if sort == "user_name":
        users = sorted(users, key=lambda x: x["user_name"].lower())

    if sort == "user_email":
        users = sorted(users, key=lambda x: x["user_email"].lower())

    users = users[skip: skip + limit]    

    return {
        "status": "success",
        "data": users
    }   

@app.get('/users/{user_name}') 
def get_user(user_name: str):
    users = read_user()

    for s in users:
        if s["user_name"].lower() == user_name.lower():
            return s

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")        

@app.post('/users' , status_code = status.HTTP_201_CREATED)   
def create_user(user:User):
    users = read_user()
    for u in users:
        if u["user_name"].lower() == user.user_name.lower():
            raise HTTPException(
                status_code=400,
                detail="Username already exists"
            )

        if u["user_email"] == user.user_email:
            raise HTTPException(
                status_code=400,
                detail="Email already exists"
            )

    new_users = jsonable_encoder(user)
    users.append(new_users)
    write_user(users)
    return {
        "status":"success",
        "data":new_users,
        "message":"user created successfully" 
    }

@app.put('/users/{user_name}')
def update_user(user_name:str,updated_user:User):
    users = read_user()
    updated_data = jsonable_encoder(updated_user)
    for user in users:
        if user['user_name'] == user_name:
            user["user_email"] = updated_data["user_email"]
            user["user_dob"] = updated_data["user_dob"]

            write_user(users)

            return {
                "status":"success",
                "data":users,
                "message":"user updated successfully"   
            }
    raise HTTPException(
        status_code=404,
        detail="User not found"
    )

@app.delete('/users/{user_name}',status_code=status.HTTP_200_OK)
def delete_user(user_name:str):
    users = read_user()
    for user in users:
        if user['user_name'] == user_name:
            users.remove(user)
            write_user(users)

            return {
                "status":"success",
                "data":users,
                "message":"user deleted successfully"   
            }
    raise HTTPException(
        status_code=404,
        detail="User not found"
    )
    

