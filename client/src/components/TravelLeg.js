import { Typography } from "@mui/material";
import React from "react";

export default function TravelLeg({ travel_leg }) {
  return (
    <Typography variant="h6">
      {travel_leg.travel_type}, {travel_leg.departure_time},{" "}
      {travel_leg.flight_number}
    </Typography>
  );
}
