import React from "react";
import { useForm } from "react-hook-form";

export default function Login() {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm();

  const onSubmit = (data) => console.log(data);

  return (
    <div className="form-dialog">
      <form onSubmit={handleSubmit(onSubmit)}>
        <label>email</label>
        <input
          type="email"
          name="email"
          {...register("email", {
            required: "email required",
          })}
        />
        {errors.email && <p className="errorMsg">{errors.email.message}</p>}
        <label>Password:</label>
        <input
          type="text"
          name="password"
          {...register("password", { required: "Password required" })}
        />
        {errors.password && (
          <p className="errorMsg">{errors.password.message}</p>
        )}
        <input type="submit" />
      </form>
    </div>
  );
}
