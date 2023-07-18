import TravelLegForm from "./TravelLegForm";
import TravelLeg from "./TravelLeg";

export default function Itineraries({ trip, currentUser, handleTravelLegAdd }) {
  return (
    <>
      <h4>itineraries:</h4>
      {trip.travel_legs?.map((travel_leg) => (
        <TravelLeg key={travel_leg.id} travel_leg={travel_leg} />
      ))}
      <TravelLegForm
        currentUser={currentUser}
        trip={trip}
        handleTravelLegAdd={handleTravelLegAdd}
      />
    </>
  );
}
