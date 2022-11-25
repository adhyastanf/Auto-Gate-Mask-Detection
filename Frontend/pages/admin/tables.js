import React from "react";

// components

import CardTable from "../../components/Cards/CardTable"

// layout for page

import Admin from "../../components/layout/layout";

export default function Tables() {
  return (
    <Admin role={"admin"}>
      <div className="flex flex-wrap mt-4">
        <div className="w-full mb-12 px-4">
          <CardTable />
        </div>
      </div>
    </Admin>
  );
}

