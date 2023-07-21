import { useContext } from "react";
import TripCard from "./TripCard";
import { UserContext } from "./UserContext";

export default function MyTrips() {
  const currentUser = useContext(UserContext);
  const trips = currentUser?.trips;
  debugger;
  return (
    <>
      <h4>Your Trips:</h4>
      {trips
        ? trips?.map((trip) => <TripCard key={trip.trip.id} trip={trip.trip} />)
        : null}
    </>
  );
}
