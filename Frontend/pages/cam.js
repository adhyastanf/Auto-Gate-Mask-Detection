import Webcam from "react-webcam";

import { useState, useEffect } from "react";

export default function Cam() {

  const [time, setTime] = useState("")

  useEffect(() => {
    const inter = setInterval(() => {
      let time = new Date();
      setTime(time.toLocaleTimeString())
    }, 1000);

  },[time])



  return (
    <section className=" h-screen ">
      <header className="h-[180px] bg-[#2CD5D9] relative">
        <p className="text-[100px] flex justify-center items-center select-none">{time}</p>
        <div className=" w-[100px] h-[100px] bg-[#D9D9D9] absolute right-[45px] top-[40px]"></div>
      </header>
      <main className="relative">
        <section className="gap-1 grid grid-cols-[repeat(2,1fr)] grid-rows-[repeat(2,405px)] box-border">
          <div className="bg-[#6E7076] p-9 relative">
            <p>CAM01</p>
            <img src="zoom.svg" alt="" className=" absolute right-[17.5px] bottom-[17.5px] z-10 cursor-pointer" draggable={false} />
          </div>
          <div className="relative overflow-hidden">
            <p className="absolute left-[9px] top-[9px] z-10">CAM02</p>
            <img src="zoom.svg" alt="" className=" absolute right-[17.5px] bottom-[17.5px] z-10 cursor-pointer" draggable={false} />
            <Webcam
              mirrored={true}
              width="100%"
              videoConstraints={{
                facingMode: "user",
              }}
              audio={false}
              video="true"
            ></Webcam>
          </div>
          <div className="relative overflow-hidden">
            <p className="absolute left-[9px] top-[9px] z-10">CAM03</p>
            <img src="zoom.svg" alt="" className=" absolute right-[17.5px] bottom-[17.5px] z-10 cursor-pointer" draggable={false} />
            <Webcam
              mirrored={true}
              width="100%"
              videoConstraints={{
                facingMode: "user",
              }}
              audio={false}
              video="true"
            ></Webcam>
          </div>
          <div className="relative overflow-hidden">
            <p className="absolute left-[9px] top-[9px] z-10">CAM04</p>
            <img src="zoom.svg" alt="" className=" absolute right-[17.5px] bottom-[17.5px] z-10 cursor-pointer" draggable={false} />
            <Webcam
              mirrored={true}
              width="100%"
              videoConstraints={{
                facingMode: "user",
              }}
              audio={false}
              video="true"
            ></Webcam>
          </div>
        </section>
        <div className=" w-[300px] h-[60px] rounded-[30px] m-auto absolute bg-white left-0 right-0 bottom-[74px]">
          <img src="square.svg" alt="" className="absolute right-5 bottom-[50%] top-[50%] translate-y-[-50%]" />
        </div>
      </main>
    </section>
  );
}
