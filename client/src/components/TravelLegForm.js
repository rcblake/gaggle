import { useContext } from "react";
import { useForm } from "react-hook-form";
import { UserContext } from "./UserContext";

export default function TravelLegForm({ trip, handleTravelLegAdd }) {
  const currentUser = useContext(UserContext);
  const {
    register,
    handleSubmit,
    reset,
    formState: { errors },
  } = useForm();

  const onSubmit = async (data) => {
    try {
      const newTravelLeg = {
        trip: {
          id: trip.id,
        },
        user: {
          id: currentUser.id,
          name: currentUser.name,
        },
        travel_type: data.travelDirection,
        departure_time: data.departureTime,
        arrival_time: data.arrivalTime,
        flight_number: data.note,
      };
      console.log(newTravelLeg);
      const postResponse = await fetch("/travel_legs", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(newTravelLeg),
      });
      if (postResponse.ok) {
        handleTravelLegAdd(newTravelLeg);
        console.log("Travel leg successfully posted to /travel_legs");
        reset();
      } else {
        console.log("Failed to post to /travel_legs");
      }
    } catch (error) {
      console.error("error while processing");
    }
  };

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
          type="datetime-local"
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
          type="datetime-local"
          name="arrivalTime"
          {...register("arrivalTime", { required: "Arrival Time is required" })}
        />
        {errors.arrivalTime && <p className="">{errors.arrivalTime.message}</p>}
        <label>Note/Flight #:</label>
        <input type="text" name="note" {...register("note", {})} />
        {errors.note && <p className="errorMsg">{errors.note.message}</p>}
        <input type="submit" />
      </form>
    </div>
  );
}
