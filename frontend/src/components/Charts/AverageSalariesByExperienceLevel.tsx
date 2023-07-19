import axios from "axios";
import React, { useState, useEffect } from "react";
import {
  Bar,
  BarChart,
  CartesianGrid,
  Legend,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";
import "./Charts.scss";

const AverageSalariesByExperienceLevel: React.FC = () => {
  const [averageSalaries, setAverageSalaries] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const { data } = await axios.get(
          "http://127.0.0.1:8000/average-salary-by-experience-level"
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
      <h1>Average Salaries By Company Size</h1>
      <ResponsiveContainer width="95%" height={300}>
        <BarChart data={averageSalaries}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="job_title" tick={{ display: "none" }} />
          <YAxis />
          <Tooltip />
          <Legend />
          <Bar dataKey="average_salary_EN" stackId="salary" fill="#ff5858" />
          <Bar dataKey="average_salary_MI" stackId="salary" fill="#ffc658" />
          <Bar dataKey="average_salary_EX" stackId="salary" fill="#82ca9d" />
          <Bar dataKey="average_salary_SE" stackId="salary" fill="#8884d8" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
};

export default AverageSalariesByExperienceLevel;
