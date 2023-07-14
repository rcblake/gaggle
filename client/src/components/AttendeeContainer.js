import React from "react";
import AttendeeForm from "./AttendeeForm";

function AttendeeContainer({ trip }) {
  const attendees = trip.users;
  return (
    <>
      {attendees.map((attendee) => (
        <p>{attendee.email}</p>
      ))}
      <AttendeeForm />
    </>
  );
}
export default AttendeeContainer;
