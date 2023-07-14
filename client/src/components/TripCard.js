import React from "react";
import { useNavigate } from "react-router-dom";

function TripCard({ trip }) {
  const navigate = useNavigate();

  const id = trip.id;

  const handleTripClick = () => {
    navigate(`/trips/${id}`);
  };

  return (
    <div onClick={handleTripClick}>
      <h5>{trip.name}</h5>
      <p>
        {trip.startDate}-{trip.endDate}
      </p>
    </div>
  );
}
export default TripCard;
