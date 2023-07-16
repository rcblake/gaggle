import React from "react";
import TravelLegForm from "./TravelLegForm";
import TravelLeg from "./TravelLeg";

function Itineraries({ trip, currentUser }) {
  return (
    <>
      <h4>itineraries:</h4>
      {trip.travel_legs?.map((travel_leg) => (
        <TravelLeg key={travel_leg.id} travel_leg={travel_leg} />
      ))}
      <TravelLegForm currentUser={currentUser} />
    </>
  );
}
export default Itineraries;
