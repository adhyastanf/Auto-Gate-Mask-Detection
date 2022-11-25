import { useRef, useState } from "react";
import axios from "axios";
import { useForm } from "react-hook-form";
import * as yup from "yup";
import { yupResolver } from "@hookform/resolvers/yup";
import Link from "next/link";

export default function Login() {
  const schema = yup
    .object()
    .shape({
      email: yup.string().email().required(),
      password: yup.string().min(4).max(15).required(),
    })
    .required();

  const { register, handleSubmit, formState:{errors} } = useForm({
    resolver: yupResolver(schema),
  });

  return (
    <section className=" flex items-center justify-center absolute left-0 right-0 top-0 bottom-0 ">
      <div className=" w-[300px]">
        <form
          id="form1"
          onSubmit={handleSubmit(async (d) => {
            const res = await axios.post("http://127.0.0.1:8000/users/login",d)
            console.log(res.data)
            // console.log(d);
            // console.log(errors)
          })}
        >
          <div className="relative mb-[14px]">
            <p className=" text-[12px] absolute -top-[10px] left-[26px] px-1 bg-white">Email</p>
            <input {...register("email")} className=" rounded-[20px] border border-solid w-full h-[40px] border-[#6E7076] px-[34px] mb-[10px]" placeholder="email" />
            <p>{errors.email?.message}</p>
          </div>
          <div className="relative mb-[14px]">
            <p className=" text-[12px] absolute -top-[10px] left-[26px] px-1 bg-white">Password</p>
            <input {...register("password")} className=" rounded-[20px] border border-solid w-full h-[40px] border-[#6E7076] px-[34px] mb-[10px]" placeholder="password" />
            <p>{errors.password?.message}</p>
          </div>
          <input type="submit" className=" rounded-[20px] border-solid w-full h-[40px] bg-[#2CD5D9] px-[34px] mb-[10px] text-white" value={"Log In"} />
          <Link href={"/signup"} ><p className="border border-[#2CD5D9] rounded-[20px] border-solid w-full h-[40px] bg-white px-[34px] mb-[10px] text-white grid place-content-center text-[#2CD5D9]">SignUp</p></Link>
        </form>
      </div>
    </section>
  );
}