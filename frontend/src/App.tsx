import React from "react";
import RemoteRatioChart from "./components/Charts/RemoteRatioChart";
import AverageSalariesChart from "./components/Charts/AverageSalariesChart";
import "./App.scss";

const App: React.FC = () => {
  return (
    <div className="app_container">
      <RemoteRatioChart />
      <AverageSalariesChart />
    </div>
  );
};

export default App;
