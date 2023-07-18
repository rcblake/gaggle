import React from "react";
import { useForm } from "react-hook-form";

export default function TripEditForm({ trip, handleTripEdit }) {
  const {
    register,
    handleSubmit,
    getValues,
    formState: { errors },
  } = useForm({
    defaultValues: {
      name: trip.name,
    },
  });

  const onSubmit = async (data) => {
    try {
      console.log(data);
      const response = await fetch(`/trips/${trip.id}`, {
        method: "PATCH",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });

      if (response.ok) {
        const trip = await response.json();
        console.log(trip);
        handleTripEdit();
      } else {
        response.json().then((err) => console.log(err.error));
      }
    } catch (error) {
      console.log("Error creating trip", error);
    }
  };

  return (
    <div className="form-dialog">
      <form onSubmit={handleSubmit(onSubmit)}>
        <label>Trip Name:</label>
        <input type="text" name="name" {...register("name", {})} />
        {errors.name && <p className="errorMsg">{errors.name.message}</p>}
        <label>Location:</label>
        <input
          defaultValue={trip.location}
          type="text"
          name="location"
          {...register("location", {})}
        />
        <label>Start Date:</label>
        <input
          defaultValue={trip.start_date}
          type="date"
          name="start_date"
          {...register("start_date", {})}
        />
        {errors.start_date && (
          <p className="errorMsg">{errors.start_date.message}</p>
        )}
        <label>End Date:</label>
        <input
          defaultValue={trip.end_date}
          type="date"
          name="end_date"
          {...register("end_date", {})}
        />
        {errors.end_date && (
          <p className="errorMsg">{errors.end_date.message}</p>
        )}
        <input type="submit" />
      </form>
    </div>
  );
}
