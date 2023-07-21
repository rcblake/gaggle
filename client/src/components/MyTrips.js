import { useContext } from "react";
import TripCard from "./TripCard";
import { UserContext } from "./UserContext";
import { Typography, Box } from "@mui/material";

export default function MyTrips() {
  const currentUser = useContext(UserContext);
  const trips = currentUser?.trips;
  return (
    <>
      <Typography marginTop={8} marginLeft={5} variant="h4">
        Your Trips:
      </Typography>
      <Box
        sx={{
          display: "flex",
          flexWrap: "wrap",
          gap: 5,
          justifyContent: "space-around",
          marginTop: 5,
          marginLeft: 8,
          marginRight: 8,
        }}
      >
        {trips
          ? trips?.map((trip) => (
              <TripCard key={trip.trip.id} trip={trip.trip} />
            ))
          : null}
      </Box>
    </>
  );
}
