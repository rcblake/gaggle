import { useState, useEffect } from "react";
import AttendeeContainer from "./AttendeeContainer";
import Itineraries from "./Itineraries";
import { useNavigate, useParams } from "react-router";

export default function Trip({ currentUser }) {
  const [trip, setTrip] = useState({});
  const navigate = useNavigate();
  const { id } = useParams();

  useEffect(() => {
    fetch(`/trips/${id}`)
      .then((res) => {
        if (res.ok) {
          return res.json();
        } else {
          throw new Error("Network response was not ok.");
        }
      })
      .then((trip) => {
        console.log(trip);
        // if (trip.users?.includes(currentUser)) {
        setTrip(trip);
        // } else {
        //   navigate("/404");
        // }
      })
      .catch((err) => {
        console.error(err);
      });
  }, [id]);
  return (
    <>
      {/* <TripHeader /> */}
      <h2>{trip.name}</h2>
      <AttendeeContainer trip={trip} />
      <Itineraries trip={trip} />
    </>
  );
}
