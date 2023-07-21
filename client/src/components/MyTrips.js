import { useContext } from "react";
import TripCard from "./TripCard";
import { UserContext } from "./UserContext";
import { Typography } from "@mui/material";

export default function MyTrips() {
  const currentUser = useContext(UserContext);
  const trips = currentUser?.trips;
  return (
    <>
      <Typography variant="h5">Your Trips:</Typography>
      {trips
        ? trips?.map((trip) => <TripCard key={trip.trip.id} trip={trip.trip} />)
        : null}
    </>
  );
}
