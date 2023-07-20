import React from "react";
import AttendeeForm from "./AttendeeForm";
import { Typography } from "@mui/material";

export default function AttendeeContainer({ trip, handleAttendeeAdd }) {
  return (
    <>
      <Typography variant="h4">attendees:</Typography>
      {trip.users?.map((user) => (
        <Typography variant="h6" key={user.user.id}>
          {user.user.email}
        </Typography>
      ))}
      <AttendeeForm trip={trip} handleAttendeeAdd={handleAttendeeAdd} />
    </>
  );
}
