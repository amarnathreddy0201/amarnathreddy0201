from fastapi import FastAPI, Depends, HTTPException, Form
from fastapi.security import OAuth2PasswordBearer
from pymongo import MongoClient
from passlib.context import CryptContext
from pydantic import BaseModel
from bson import ObjectId
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder

import requests
import cv2
import base64

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["fastapi_example"]
users_collection = db["users"]

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 password flow for authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# Pydantic model for user registration
class UserRegister(BaseModel):
    username: str
    password: str
    city: Optional[str]


# Pydantic model for user login
class UserLogin(BaseModel):
    username: str
    password: str


# Pydantic model for forgot password
class ForgotPassword(BaseModel):
    email: str


# User model
class User:
    def __init__(self, username: str, hashed_password: str, id: ObjectId):
        self.id = id
        self.username = username
        self.hashed_password = hashed_password


def userEntity(user) -> dict:
    print("userEntity : ", user)
    return {
        "id": str(user["_id"]),
        "username": user["username"],
        "hashed_password": user["hashed_password"],
        "city": user["city"],
    }


def userListEntity(users) -> list:
    return [userEntity(user) for user in users]


# Function to create a new user
def create_user(username: str, password: str, city: str):
    hashed_password = pwd_context.hash(password)
    user_data = {"username": username, "hashed_password": hashed_password, "city": city}
    result = users_collection.insert_one(user_data)
    return User(username, hashed_password, result.inserted_id)


# Function to get a user by username
async def get_user(username: str):
    user_data = users_collection.find({"username": username})

    return userListEntity(user_data)


# Function to verify user credentials
async def verify_user_credentials(username: str, password: str):
    users = await get_user(username)

    for user in users:
        if user["username"] == username and pwd_context.verify(
            password, user["hashed_password"]
        ):
            return user

    return "user not found"


async def verify_user(username: str):
    users = await get_user(username)
    for user in users:
        if user["username"] == username:
            return f"User already exist: {user['username']}"

    else:
        return None


# Dependency to get the current user based on the OAuth2 token
def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Invalid credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    user = verify_user_credentials(token, token)
    if user is None:
        raise credentials_exception
    return user


# Endpoint to register a new user
@app.post("/register")
async def register(user_data: UserRegister):
    user_exist = await verify_user(user_data.username)
    if user_exist:
        return {"message": "User already exist"}
    else:
        user = create_user(user_data.username, user_data.password, user_data.city)
        return {"new user created": user.username}


# Endpoint to login and obtain a token
@app.post("/login")
async def login(user_data: UserLogin):
    print("user_data while login: ", user_data, "line no : ", 121)
    user = await verify_user_credentials(user_data.username, user_data.password)

    if user is None:
        return {"message": "Invalid username or password"}
    return {
        "token": user
    }  # In a real scenario, you would generate and return a JWT token


# Endpoint for password recovery (dummy implementation)
@app.post("/forgot-password")
async def forgot_password(forgot_data: ForgotPassword):
    user = get_user(forgot_data.email)
    if user:
        # In a real scenario, you would send an email with a unique link for password reset
        return {"message": "Password reset link sent to your email"}
    else:
        raise HTTPException(status_code=404, detail="User not found")


# # Protected endpoint that requires authentication
# @app.get("/protected")
# async def protected_route(current_user: User = Depends(get_current_user)):
#     return {"message": "This is a protected route", "username": current_user.username}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("user_crediantals:app", host="127.0.0.1", port=8000, reload=True)
