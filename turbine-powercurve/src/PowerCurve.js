import React, { useState, useEffect } from "react";
import axios from "axios";
import { ScatterChart, Scatter, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from "recharts";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";

export default function PowerCurve() {
  const [startDate, setStartDate] = useState(new Date("2016-01-01"));
  const [endDate, setEndDate] = useState(new Date("2016-12-31"));
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(false);
  const [turbineId, setTurbineId] = useState(1);
  const [turbineData, setTurbineData] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/turbine_data/?turbine_id=1")
      .then(res => res.json())
      .then(data => {
        console.log("Fitched data:  ", data);
        setTurbineData(data.data)})
      .catch(err => console.error("Fetch error:", err));
  }, []);

  const fetchData = async () => {
    setLoading(true);
    try {
      const startISO = startDate.toISOString().slice(0, 19);
      const endISO = endDate.toISOString().slice(0, 19);

      const res = await axios.get("http://localhost:8000/turbine_data/", {
        params: {
          turbine_id: turbineId,
          start_time: startISO,
          end_time: endISO,
          limit: 500
        }
      });

      const points = res.data.data
        .filter(d => d["m/s"] && d["kW"])
        .map(d => ({ windSpeed: d["m/s"], power: d["kW"] }));

      setData(points);
    } catch (err) {
      console.error("Error fetching turbine data", err);
      setData([]);
    }
    setLoading(false);
  };

  useEffect(() => {
    fetchData();
  }, [startDate, endDate, turbineId]);

  return (
    <div style={{ maxWidth: 800, margin: "auto", padding: 20 }}>
      <h2>Turbine Power Curve (Power vs Wind Speed)</h2>

      <div style={{ marginBottom: 20 }}>
        <label>Select Turbine: </label>
        <select value={turbineId} onChange={e => setTurbineId(Number(e.target.value))}>
          <option value={1}>Turbine 1</option>
          <option value={2}>Turbine 2</option>
        </select>
      </div>
      
      <div style={{ marginBottom: 20, display: "flex", gap: 10, alignItems: "center" }}>
        <div>
          <label>Start Date: </label>
          <DatePicker selected={startDate} onChange={date => setStartDate(date)} />
        </div>
        <div>
          <label>End Date: </label>
          <DatePicker selected={endDate} onChange={date => setEndDate(date)} />
        </div>
      </div>

      {loading ? (
        <p>Loading data...</p>
      ) : data.length === 0 ? (
        <p>No data available for selected range.</p>
      ) : (
        <ResponsiveContainer width="100%" height={400}>
          <ScatterChart>
            <CartesianGrid />
            <XAxis type="number" dataKey="windSpeed" name="Wind Speed (m/s)" />
            <YAxis type="number" dataKey="power" name="Power (kW)" />
            <Tooltip cursor={{ strokeDasharray: "3 3" }} />
            <Scatter name="Power Curve" data={data} fill="#8884d8" />
          </ScatterChart>
        </ResponsiveContainer>
      )}
    </div>
  );
}
