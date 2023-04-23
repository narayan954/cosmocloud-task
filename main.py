from fastapi import FastAPI, HTTPException
from pymongo import MongoClient

# fix ObjectId & FastApi conflict
import pydantic
from bson.objectid import ObjectId
pydantic.json.ENCODERS_BY_TYPE[ObjectId] = str

app = FastAPI()
client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]

# users collection
users = db["users"]

# orgs collection
orgs = db["orgs"]

# root endpoint


@app.get("/")
def read_root():
    return {"Hello": "World"}

# Create a new User


@app.post("/users")
async def create_user(user: dict):
    result = users.insert_one(user)
    return {"id": str(result.inserted_id), **user}

# List all users in the system


@app.get("/users")
async def get_all_users(offset: int = 0, limit: int = 100, name: str = ""):
    query = {}
    if name:
        query["name"] = name

    users_count = users.count_documents(query)
    users_list = list(users.find(query, {"_id": 0}).skip(offset).limit(limit))

    return {"total_count": users_count, "users": users_list}


# Fetch a single User


@app.get("/users/{user_id}")
async def get_user(user_id: str):
    result = users.find_one({"_id": ObjectId(user_id)})
    return result if result else {"message": "User not found"}


# Create a new Organisation

@app.post("/orgs")
async def create_org(org: dict):
    if orgs.find_one(org):
        raise HTTPException(
            status_code=400, detail="Organization already exists")
    result = orgs.insert_one(org)
    return {"id": str(result.inserted_id), **org}

# List all organisation


@app.get("/orgs")
async def get_all_orgs(offset: int = 0, limit: int = 100, name: str = ""):
    if name:
        query = {"name": {"$regex": name, "$options": "i"}}
    else:
        query = {}
    orgs = db.orgs.find(query, {"_id": 0}).skip(offset).limit(limit)
    total_count = db.orgs.count_documents(query)
    return {"total_count": total_count, "items": list(orgs)}
