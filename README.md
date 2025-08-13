Turbine Data Analytics — FastAPI + MongoDB + React

This project provides a full-stack solution to store, query, and visualize wind turbine performance data.


Features

Backend

Python FastAPI services with MongoDB for data storage and aggregation.
Turbine Data API (load_turbine_data.py)
Load CSV data for multiple turbines into MongoDB.
Query turbine data by ID, date range, and limit.
JSON serialization for datetime and MongoDB ObjectIds.
Post/Comment Aggregator (load_data.py + main.py)
Fetches demo posts/comments from JSONPlaceholder API.
Aggregates number of posts per user and comments per post.

Frontend

React app with interactive charts for visualizing turbine power curves.
Date pickers and turbine selectors to filter data.


Tech Stack

Backend: FastAPI, MongoDB
Frontend: React
Infrastructure: Docker Compose

Project Structure
.
├── backend/
│   ├── load_data.py           # Loads posts/comments from JSONPlaceholder into MongoDB
│   ├── main.py                # FastAPI app for posts/comments aggregation
│   ├── load_turbine_data.py   # Loads turbine CSV data & serves turbine API
│   ├── docker-compose.yml     # MongoDB container configuration
│
├── frontend/
│   ├── App.js                 # Main React entry
│   ├── PowerCurve.js          # Power curve chart component

Getting Started

1.Clone the repository
git clone https://github.com/Sham-Hs/turbit.git
2.Start MongoDB
docker-compose up -d
3.Install Backend Dependencies
pip install fastapi uvicorn pymongo requests pandas
4.Load Sample Data
For turbine data (CSV files required):
python load_turbine_data.py
For posts/comments demo:
python load_data.py
5.Run Backend API
Run turbine data API:
uvicorn load_turbine_data:app --reload
Run posts/comments API:
uvicorn main:app --reload
Running the Frontend
npm install
npm start

