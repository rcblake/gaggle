import React from "react";

import TripCard from "./TripCard";
import { useNavigate } from "react-router";

export default function Home({ currentUser }) {
  const navigate = useNavigate();
  const trips = currentUser?.trips;

  const handleAddClick = (e) => {
    const id = e.target.id;
    navigate("/trip_form", { id });
  };

  return (
    <>
      <button onClick={handleAddClick}>Plan a trip</button>
      {/* <div>
        {trips.map((trip) => (
          <TripCard key={trip.id} trip={trip} />
        ))}
      </div> */}
    </>
  );
}
