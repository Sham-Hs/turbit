import requests
from pymongo import MongoClient

# Connention to MongoDB
client = MongoClient("mongodb://root:Task@localhost:27017/")
db = client["mydatabase"]

# define Collections 
posts_collection = db["posts"]
comments_collection = db["comments"]

# Fetch Data from API
posts = requests.get("https://jsonplaceholder.typicode.com/posts").json()
comments = requests.get("https://jsonplaceholder.typicode.com/comments").json()


# 3. remove/ add data
posts_collection.delete_many({})
comments_collection.delete_many({})

posts_collection.insert_many(posts)
comments_collection.insert_many(comments)

print("Data has been loaded into MongoDB")
