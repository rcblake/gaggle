import React from "react";
import { useForm } from "react-hook-form";
import { useNavigate } from "react-router";

export default function TripForm() {
  const {
    register,
    handleSubmit,
    getValues,
    reset,
    formState: { errors },
  } = useForm();
  const navigate = useNavigate();

  const onSubmit = async (data) => {
    try {
      console.log(data);
      const response = await fetch("/trips", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });

      if (response.ok) {
        const trip = await response.json();
        navigate(`/trips/${trip.id}`);
      } else {
        console.log("Error creating trip");
      }
    } catch (error) {
      console.log("Error creating trip", error);
    }
  };

  return (
    <div className="form-dialog">
      <form onSubmit={handleSubmit(onSubmit)}>
        <label>Trip Name:</label>
        <input
          type="text"
          name="name"
          {...register("name", {
            required: "Name is required",
          })}
        />
        {errors.name && <p className="errorMsg">{errors.name.message}</p>}
        <label>Location:</label>
        <input type="text" name="location" {...register("location", {})} />
        <label>Start Date:</label>
        <input
          type="date"
          name="start_date"
          {...register("start_date", {
            required: "Start Date is required",
          })}
        />
        {errors.start_date && (
          <p className="errorMsg">{errors.start_date.message}</p>
        )}
        <label>End Date:</label>
        <input
          type="date"
          name="end_date"
          {...register("end_date", {
            required: "End Date is required",
            validate: (value) => value > getValues().start_date,
          })}
        />
        {errors.end_date && (
          <p className="errorMsg">{errors.end_date.message}</p>
        )}
        <input type="submit" />
      </form>
    </div>
  );
}
