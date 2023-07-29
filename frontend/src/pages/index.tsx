import AverageSalariesByCompanySize from "@/components/Charts/AverageSalariesByCompanySize";
import AverageSalariesByExperienceLevel from "@/components/Charts/AverageSalariesByExperienceLevel";
import RemoteRatioChart from "@/components/Charts/RemoteRatioChart";
import { useAuth0 } from "@auth0/auth0-react";
import "./App.scss";
import { useEffect } from "react";

export default function Page() {
  const { getAccessTokenSilently } = useAuth0();

  const fetchData = async () => {
    try {
      const accessToken = await getAccessTokenSilently();
      // Use the accessToken for API requests or pass it to the backend.
      console.log("Access Token:", accessToken);
    } catch (error) {
      console.error("Error getting access token:", error);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

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
