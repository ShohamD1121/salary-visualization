import React from "react";
import RemoteRatioChart from "./components/Charts/RemoteRatioChart";
import AverageSalariesByCompanySize from "./components/Charts/AverageSalariesByCompanySize";
import AverageSalariesByExperienceLevel from "./components/Charts/AverageSalariesByExperienceLevel";
import "./App.scss";

const App: React.FC = () => {
  return (
    <div className="app_container">
      <h1>Data Salaries</h1>
      <div className="charts_container">
        <AverageSalariesByExperienceLevel />
        <AverageSalariesByCompanySize />
        <RemoteRatioChart />
      </div>
    </div>
  );
};

export default App;
