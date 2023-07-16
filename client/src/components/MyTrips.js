import React from "react";
import TripCard from "./TripCard";

export default function MyTrips({ currentUser }) {
  const trips = currentUser?.trips;

  return (
    <>
      <h4>Your Trips:</h4>
      {trips?.map((trip) => (
        <TripCard key={trip.trip.id} trip={trip.trip} />
      ))}
    </>
  );
}
