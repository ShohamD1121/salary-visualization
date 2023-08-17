import React, { useState, useEffect } from "react";
import axios from "axios";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";
import "./Charts.scss";

const RemoteRatioChart: React.FC = () => {
  const [remoteRatios, setRemoteRatios] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const { data } = await axios.get("http://127.0.0.1:8000/remote-ratios");
        setRemoteRatios(data);
      } catch (error) {
        console.log("Error fetching remote ratios:", error);
      }
    };

    fetchData();
  }, []);

  return (
    <div className="chart-container">
      <h1>Remote Ratio</h1>
      <ResponsiveContainer width="95%" height={300}>
        <BarChart data={remoteRatios}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="remote_ratio" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Bar dataKey="count" fill="#8884d8" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
};

export default RemoteRatioChart;
