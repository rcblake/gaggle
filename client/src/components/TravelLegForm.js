import React from "react";
import { useForm } from "react-hook-form";

export default function TravelLegForm() {
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
        <label>Travel Direction</label>
        <select
          name="travelDirection"
          {...register("travelDirection", {
            required: "Select travel direction",
          })}
        >
          <option value="" disabled>
            Select:
          </option>
          <option value="Depart">Depart</option>
          <option value="Return">Return</option>
        </select>
        <label>Departure Time:</label>
        <input
          type="dateTime"
          name="departureTime"
          {...register("departureTime", {
            required: "Departure Time is required",
          })}
        />
        {errors.departureTime && (
          <p className="">{errors.departureTime.message}</p>
        )}
        <label>Arrival Time:</label>
        <input
          type="dateTime"
          name="arrivalTime"
          {...register("arrivalTime", { required: "Arrival Time is required" })}
        />
        {errors.arrivalTime && <p className="">{errors.arrivalTime.message}</p>}
        <label>Note:</label>
        <input type="text" name="note" {...register("note", {})} />
        {errors.note && <p className="errorMsg">{errors.note.message}</p>}
        <input type="submit" />
      </form>
    </div>
  );
}
