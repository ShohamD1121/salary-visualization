import AverageSalariesByCompanySize from "@/components/Charts/AverageSalariesByCompanySize";
import AverageSalariesByExperienceLevel from "@/components/Charts/AverageSalariesByExperienceLevel";
import RemoteRatioChart from "@/components/Charts/RemoteRatioChart";
import "./App.scss";

export default function Page() {
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
}
