import React from "react";
import AttendeeForm from "./AttendeeForm";

export default function AttendeeContainer({ trip, handleAttendeeAdd }) {
  return (
    <>
      <h4>attendees:</h4>
      {trip.users?.map((user) => (
        <p key={user.user.id}>{user.user.email}</p>
      ))}
      <AttendeeForm trip={trip} handleAttendeeAdd={handleAttendeeAdd} />
    </>
  );
}
