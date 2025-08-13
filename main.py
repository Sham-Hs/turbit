from fastapi import FastAPI
from pymongo import MongoClient
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Connecting to MongoDB 
client = MongoClient("mongodb://r" \
"oot:Task@localhost:27017/")
db = client["mydatabase"]

@app.get("/")
def home():
    return {"message": "FastAPI MongoDB API running!"}

@app.get("/posts-per-user")
def posts_per_user():
    pipeline = [
        {"$group": {"_id": "$userId", "total_posts": {"$sum": 1}}},
        {"$sort": {"_id": 1}}
    ]
    result = list(db["posts"].aggregate(pipeline))
    return {"posts_per_user": result}

@app.get("/comments-per-post")
def comments_per_post():
    pipeline = [
        {"$group": {"_id": "$postId", "total_comments": {"$sum": 1}}},
        {"$sort": {"_id": 1}}
    ]
    result = list(db["comments"].aggregate(pipeline))
    return {"comments_per_post": result}
