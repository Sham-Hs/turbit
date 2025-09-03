<h2>Turbine Data Analytics — FastAPI + MongoDB + React</h2>

This project provides a full-stack solution to store, query, and visualize wind turbine performance data.


<h3>Features</h3>

<h5>Backend: </h5>
Python FastAPI services with MongoDB for data storage and aggregation.<br>
Turbine Data API (load_turbine_data.py)<br>
Load CSV data for multiple turbines into MongoDB.<br>
Query turbine data by ID, date range, and limit.<br>
JSON serialization for datetime and MongoDB ObjectIds.<br>
Post/Comment Aggregator (load_data.py + main.py)<br>
Fetches demo posts/comments from JSONPlaceholder API.<br>
Aggregates number of posts per user and comments per post.<br>

<h5>Frontend:</h5>
React app with interactive charts for visualizing turbine power curves.
Date pickers and turbine selectors to filter data.


<h3>Tech Stack</h3>

Backend: FastAPI, MongoDB
Frontend: React
Infrastructure: Docker Compose

<h3>Project Structure</h3>
.<br>
├── backend/<br>
│   ├── load_data.py           # Loads posts/comments from JSONPlaceholder into MongoDB<br>
│   ├── main.py                # FastAPI app for posts/comments aggregation<br>
│   ├── load_turbine_data.py   # Loads turbine CSV data & serves turbine API<br>
│   ├── docker-compose.yml     # MongoDB container configuration<br>
│
├── frontend/<br>
│   ├── App.js                 # Main React entry<br>
│   ├── PowerCurve.js          # Power curve chart component<br>

<h3>Getting Started</h3>

1.Clone the repository<br>
<pre>git clone https://github.com/Sham-Hs/turbit.git</pre>
2.Start MongoDB<br>
<pre> docker-compose up </pre>
3.Install Backend Dependencies<br>
<pre>pip install fastapi uvicorn pymongo requests pandas</pre>
4.Load Sample Data<br>
For turbine data (CSV files required):<br>
<pre>python load_turbine_data.py</pre>
For posts/comments demo:<br>
<pre>python load_data.py</pre>
5.Run Backend API<br>
Run turbine data API:<br>
<pre>uvicorn load_turbine_data:app --reload</pre>
Run posts/comments API:<br>
<pre>uvicorn main:app --reload</pre>
Running the Frontend<br>
<pre>npm install</pre>
<pre>npm start</pre>

