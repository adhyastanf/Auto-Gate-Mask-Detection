import React from "react";

// components

import AdminNavbar from "../Navbars/AdminNavbar";
import Sidebar from "../Sidebar/Sidebar";
import HeaderStats from "../Headers/HeaderStats";
import FooterAdmin from "../Footers/FooterAdmin";

export default function Admin({ children, role }) {
  return (
    <div className=" font-[Helvetica]">
      <Sidebar role={role} />
      <div className="relative md:ml-64 ">
        <AdminNavbar />
        {/* Header */}
        <HeaderStats />
        <div className="px-4 md:px-10 mx-auto w-full -m-24">
          {children}
          <FooterAdmin />
        </div>
      </div>
    </div>
  );
}
