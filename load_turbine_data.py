import pandas as pd
from pymongo import MongoClient
from fastapi import FastAPI, HTTPException, Query
from typing import Optional
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware



# connection
client = MongoClient("mongodb://root:Task@localhost:27017/")
db = client["mydatabase"]

# Testing
count = db.turbine_data.count_documents({})
print(f"Total documents in turbine_data: {count}")

sample = db.turbine_data.find_one()
print("Sample document:", sample)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Turbine Data API running!"}

@app.get("/turbine_data/")
def get_turbine_data(
    turbine_id: int = Query(..., description="ID of the turbine"),
    start_time: Optional[datetime] = Query(None, description="Start datetime in ISO format"),
    end_time: Optional[datetime] = Query(None, description="End datetime in ISO format"),
    limit: int = Query(500, description="Max number of records to return"),
):  
    query = {"turbine_id": turbine_id}

    if start_time or end_time:
        query["Dat/Zeit_main"] = {}
        if start_time:
            query["Dat/Zeit_main"]["$gte"] = start_time
        if end_time:
            query["Dat/Zeit_main"]["$lte"] = end_time
        if not query["Dat/Zeit_main"]:  
            del query["Dat/Zeit_main"]

    cursor = db.turbine_data.find(query).limit(limit)
    results = list(cursor)

    # Convert MongoDB ObjectId and datetime to str for JSON serialization
    for r in results:
        r["_id"] = str(r["_id"])
        if "Dat/Zeit_main" in r and r["Dat/Zeit_main"]:
            r["Dat/Zeit_main"] = r["Dat/Zeit_main"].isoformat()
    
    if not results:
        raise HTTPException(status_code=404, detail="No data found for the given query")

    return {"count": len(results), "data": results}


def load_csv_to_mongo(file_path, turbine_id):
    df = pd.read_csv(file_path, sep=';', decimal=',', skiprows=1, header=0)
    
    # Clean column names
    df.columns = df.columns.str.strip()
    
    # Rename first date column
    df.rename(columns={df.columns[0]: "Dat/Zeit"}, inplace=True)
    
    # Handle duplicate columns and set a main datetime column
    cols = df.columns.tolist()
    first_date_idx = next((i for i, col in enumerate(cols) if col == "Dat/Zeit"), None)
    if first_date_idx is None:
        raise ValueError("No 'Dat/Zeit' column found")
    cols[first_date_idx] = "Dat/Zeit_main"
    df.columns = cols

    # Convert to datetime
    df["Dat/Zeit_main"] = pd.to_datetime(df["Dat/Zeit_main"], dayfirst=True, errors='coerce')

    # Add turbine ID
    df["turbine_id"] = turbine_id

    # Connect to MongoDB
    client = MongoClient("mongodb://root:Task@localhost:27017/")
    db = client["mydatabase"]
    collection = db["turbine_data"]

    # Insert into MongoDB
    records = df.to_dict(orient="records")
    collection.insert_many(records)
    print(f"{len(records)} records inserted for turbine {turbine_id}")

if __name__ == "__main__":
    import uvicorn

    load_csv_to_mongo("Turbine1.csv", 1)
    load_csv_to_mongo("Turbine2.csv", 2)