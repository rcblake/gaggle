import React from "react";
import AttendeeForm from "./AttendeeForm";
import { Typography, Box } from "@mui/material";

export default function AttendeeContainer({ trip, handleAttendeeAdd }) {
  return (
    <Box sx={{ display: "flex", flexDirection: "column" }}>
      <Typography variant="h4">attendees</Typography>
      {trip.users?.map((user) => (
        <Typography variant="body1" key={user.user.id}>
          {user.user.name}
        </Typography>
      ))}
      <AttendeeForm trip={trip} handleAttendeeAdd={handleAttendeeAdd} />
    </Box>
  );
}
