import React from "react";
import { useForm } from "react-hook-form";

export default function TripForm() {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm();

  const onSubmit = (data) => console.log(data);
  console.log(errors);

  return (
    <div className="form-dialog">
      <form onSubmit={handleSubmit(onSubmit)}>
        <label>Trip Name:</label>
        <input
          type="text"
          name="tripName"
          {...register("tripName", {
            required: "Name is required",
          })}
        />
        {errors.tripName && (
          <p className="errorMsg">{errors.tripName.message}</p>
        )}
        <label>Location:</label>
        <input type="text" name="location" {...register("location", {})} />
        <label>Start Date:</label>
        <input
          type="date"
          name="startDate"
          {...register("startDate", {
            required: "Start Date is required",
          })}
        />
        {errors.startDate && (
          <p className="errorMsg">{errors.startDate.message}</p>
        )}
        <label>End Date:</label>

        <input
          type="date"
          name="endDate"
          {...register("endDate", {
            required: "End Date is required",
          })}
        />
        {errors.endDate && <p className="errorMsg">{errors.endDate.message}</p>}
        <input type="submit" />
      </form>
    </div>
  );
}
