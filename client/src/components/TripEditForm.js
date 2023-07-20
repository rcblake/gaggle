import React from "react";
import { useForm, useFormState } from "react-hook-form";

export const dirtyValues = (dirtyFields, allValues) => {
  if (dirtyFields === true || Array.isArray(dirtyFields)) {
    return allValues;
  }

  return Object.fromEntries(
    Object.keys(dirtyFields).map((key) => [
      key,
      dirtyValues(dirtyFields[key], allValues[key]),
    ])
  );
};

export default function TripEditForm({ trip, handleTripEdit }) {
  const {
    register,
    handleSubmit,
    formState,
    getValues,
    formState: { errors },
  } = useForm({
    mode: "onChange",
    defaultValues: {
      name: trip?.name,
      location: trip?.location,
      start_date: trip?.start_date,
      end_date: trip?.end_date,
    },
  });

  const onSubmit = async (data) => {
    try {
      console.log(dirtyValues(formState.dirtyFields, data));
      const tripEdit = dirtyValues(formState.dirtyFields, data);
      const response = await fetch(`/trips/${trip.id}`, {
        method: "PATCH",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(tripEdit),
      });

      if (response.ok) {
        const trip = await response.json();
        console.log(trip);
        handleTripEdit();
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
          defaultValue={trip.name}
          type="text"
          name="name"
          {...register("name", {})}
        />
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
          {...register("end_date", {
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
