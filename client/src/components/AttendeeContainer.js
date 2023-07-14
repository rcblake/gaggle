import React from "react";
import AttendeeForm from "./AttendeeForm";

export default function AttendeeContainer({ trip }) {
  return (
    <>
      {/* {trip.users.map((user) => (
        <p key={user.user.id}>{user.user.email}</p>
      ))} */}
      <AttendeeForm trip={trip} />
    </>
  );
}
