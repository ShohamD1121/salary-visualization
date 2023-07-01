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

const AverageSalariesChart: React.FC = () => {
  const [averageSalaries, setAverageSalaries] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const { data } = await axios.get(
          "http://127.0.0.1:8000/salaries-average"
        );
        setAverageSalaries(data);
      } catch (error) {
        console.log("Error fetching data:", error);
      }
    };

    fetchData();
  }, []);

  return (
    <div className="chart-container">
      <h1>Average Salary Chart</h1>
      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={averageSalaries}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="job_title" tick={{ display: "none" }} />
          <YAxis />
          <Tooltip />
          <Legend />
          <Bar dataKey="salary_L" stackId="salary" fill="#8884d8" />
          <Bar dataKey="salary_M" stackId="salary" fill="#82ca9d" />
          <Bar dataKey="salary_S" stackId="salary" fill="#ffc658" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
};

export default AverageSalariesChart;
