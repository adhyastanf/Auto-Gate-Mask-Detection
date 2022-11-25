import React, { useState } from "react";
import data from "../../libs/db";
import ExportExcel from "../exportExcel";
import { useRef } from "react";

// components

import TableDropdown from "../Dropdowns/TableDropdown";

export default function CardTable() {
  const select = useRef();
  const [selectValue, setSelectValue] = useState("");
  const [date, setDate] = useState("")
  // console.log(date)

  return (
    <>
      <div className={"relative flex flex-col min-w-0 break-words w-full mb-6 shadow rounded bg-white "}>
        <div className="rounded-t mb-0 px-4 py-3 border-0">
          <div className="flex flex-wrap items-center justify-between">
            <h3 className={"font-semibold text-lg "}>User Tables</h3>
            <div>
              <input type="date" name="date" id="" onChange={e => setDate(e.target.value)}  />
              <select ref={select} name="" id="" defaultValue={""} onChange={(e) => setSelectValue(e.target.value)}>
                <option value="">All</option>
                <option value="5">5</option>
                <option value="10">10</option>
                <option value="15">15</option>
              </select>
              <ExportExcel excelData={data} fileName={"exportExcel"} />
            </div>
            {/* <div className="relative w-full px-4 max-w-full ">
            </div> */}
          </div>
        </div>
        <div className="block w-full overflow-x-auto">
          {/* Projects table */}
          <table className="items-center w-full bg-transparent border-collapse">
            <thead>
              <tr className=" bg-pmLight/50">
                <th className={"px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left "}>Nama Depan</th>
                <th className={"px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left "}>Nama Belakang</th>
                <th className={"px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left "}>Birthdate</th>
                <th className={"px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left "}>Gender</th>
                <th className={"px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left "}>Username</th>
                <th className={"px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left "}></th>
              </tr>
            </thead>
            <tbody>
              {data
                .filter((data) => date === ""?data:data.birthdate === date)
                .slice(0, selectValue == "" ? undefined : selectValue)
                .map((data, index) => {
                  return (
                    <tr key={index}>
                      <th className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4 text-left flex items-center">{data.namadepan}</th>
                      <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4">{data.namabelakang}</td>
                      <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4">{data.birthdate}</td>
                      <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4">{data.gender}</td>
                      <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4">{data.username}</td>
                      <td className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4 text-right">
                        <TableDropdown />
                      </td>
                    </tr>
                  );
                })}
            </tbody>
          </table>
        </div>
      </div>
    </>
  );
}
