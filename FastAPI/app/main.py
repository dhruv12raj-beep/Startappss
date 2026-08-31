from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel 
from app.schemas.user import UserCreate

app = FastAPI()

    
@app.get('/users') #path parameter
def home():
    return {"message" : "hello fastapi"}

@app.get("/users/{user_id}") 
def get_user(name:str, age: int):
    return {"message":f"Usersname: {name} and age:{age}fetched successfully."} 

#server/users/1
#local/user?name=abc&age=25&limit=106&page

@app.post('/users')
def create_user(user : UserCreate):
    return {
        "message":"User received successfully",
        "user": user.model_dump()
    } 

@app.put('/users')
def update_user():
    return {"message" : "Update Users"} 


@app.delete('/users')
def put_user():
    return {"message" : "Delete Users"} 



#type hints: use for validation, documentation, request, parsing 
# 
# two types of server: UVicorn (FastAPi) ASGI , Django gunicorn WSGI  
# [path parameters are dynamic like user id or any other datatype]
# query parameters are used for searching , sorting and filtering and pagination.
