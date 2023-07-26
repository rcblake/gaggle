import React from "react";
import { useNavigate } from "react-router-dom";
import Card from "@mui/material/Card";
import CardActions from "@mui/material/CardActions";
import CardContent from "@mui/material/CardContent";
import { Typography, Box, Button } from "@mui/material";

function TripCard({ trip }) {
  const navigate = useNavigate();
  debugger;
  const id = trip.id;

  const handleTripClick = () => {
    navigate(`/trips/${id}`);
  };
  return (
    <Card sx={{ width: 200 }} onClick={handleTripClick}>
      <CardContent>
        <Typography variant="h5" component="div">
          {trip.name}
        </Typography>
        <Typography sx={{ mb: 1.5 }} color="text.secondary">
          {trip.location}
        </Typography>
        <Typography variant="body2">
          {trip.start_date}-{trip.end_date}
        </Typography>
      </CardContent>
      <CardActions>
        <Button size="small">View Trip</Button>
      </CardActions>
    </Card>
  );
}
export default TripCard;
