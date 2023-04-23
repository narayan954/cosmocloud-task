from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()
client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
users = db["users"]

# root endpoint
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Create a new User
@app.post("/users")
async def create_user(user: dict):
    result = users.insert_one(user)
    return {"id": str(result.inserted_id)}

# List all users in the system
@app.get("/users")
async def get_all_users(offset: int = 0, limit: int = 100, name: str = ""):
    if name:
        return list(users.find({"name": name}, {"_id": 0}).skip(offset).limit(limit))
    return list(users.find({}, {"_id": 0}).skip(offset).limit(limit))
