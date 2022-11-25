import React from "react";

// components

import CardLineChart from "../../components/Cards/CardLineChart";
import CardBarChart from "../../components/Cards/CardBarChart";
import CardPageVisits from "../../components/Cards/CardPageVisits";
import CardSocialTraffic from "../../components/Cards/CardSocialTraffic";
import Admin from "../../components/layout/layout";

// layout for page

// import Admin from "layouts/Admin.js";

export default function Dashboard() {
  return (
    <Admin role={"security"}>
      <div className="flex justify-center ">
        <div className="w-full xl:w-8/12 mb-12 xl:mb-0 px-4 ">
          <CardLineChart />
        </div>
        {/* <div className="w-full xl:w-4/12 px-4">
          <CardBarChart />
        </div> */}
      </div>
      <div className="flex flex-wrap mt-4">
        <div className="w-full xl:w-8/12 mb-12 xl:mb-0 px-4">
          <CardPageVisits />
        </div>
        <div className="w-full xl:w-4/12 px-4">
          <CardSocialTraffic />
        </div>
      </div>
    </Admin>
  );
}


