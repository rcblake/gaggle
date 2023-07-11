import React from "react";
import { useForm } from "react-hook-form";

export default function AttendeeForm() {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm();

  const onSubmit = (data) => console.log(data);
  console.log(errors);

  return (
    <div>
      <form onSubmit={handleSubmit(onSubmit)}>
        <label>email:</label>
        <input
          type="email"
          name="email"
          {...register("email", {
            required: "email is required",
          })}
        />
        {errors.email && <p className="errorMsg">{errors.email.message}</p>}
        <input type="submit" />
      </form>
    </div>
  );
}
