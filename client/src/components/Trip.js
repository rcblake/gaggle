import { useState } from "react";
import AttendeeContainer from "./AttendeeContainer";
import Itineraries from "./Itineraries";
import { useNavigate } from "react-router";

function Trip({ currentUser }) {
  const { trip, setTrip } = useState({});
  const navigate = useNavigate();

  fetch("/trips/:id")
    .then((res) => res.json())
    .then((trip) => {
      debugger;
      if (currentUser in trip?.users) {
        setTrip(trip);
      } else {
        navigate("/404");
      }
    });

  return (
    <>
      {/* <TripHeader /> */}
      <AttendeeContainer trip={trip} />
      <Itineraries trip={trip} />
    </>
  );
}
export default Trip;
