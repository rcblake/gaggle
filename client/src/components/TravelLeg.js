import React from "react";

export default function TravelLeg({ travel_leg }) {
  return (
    <>
      <p key={travel_leg.id}>
        {travel_leg.travel_type}, {travel_leg.departure_time}
      </p>
    </>
  );
}
