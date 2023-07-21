import { Typography } from "@mui/material";
import React from "react";
import { useNavigate } from "react-router-dom";

function TripCard({ trip }) {
  const navigate = useNavigate();

  const id = trip.id;

  const handleTripClick = () => {
    navigate(`/trips/${id}`);
  };

  return (
    <div style={{ gap: 5, margin: (20, 20, 20, 20) }} onClick={handleTripClick}>
      <Typography>{trip.name}</Typography>
      <Typography>{trip.location}</Typography>
      <Typography>
        {trip.start_date} - {trip.end_date}
      </Typography>
    </div>
  );
}
export default TripCard;
