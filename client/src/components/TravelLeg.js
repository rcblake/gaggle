import React from "react";

export default function TravelLeg({ travel_leg }) {
  return (
    <p>
      {travel_leg.travel_type}, {travel_leg.departure_time},{" "}
      {travel_leg.flight_number}
    </p>
  );
}
