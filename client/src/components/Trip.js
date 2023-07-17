import { useState, useEffect } from "react";
import AttendeeContainer from "./AttendeeContainer";
import Itineraries from "./Itineraries";
import { useNavigate, useParams } from "react-router";
import TripEditForm from "./TripEditForm";

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

  const handleEdit = () => {};
  const handleDelete = () => {};

  return (
    <>
      {/* <TripHeader /> */}
      <h2>Trip:{trip.name}</h2>
      Edit:
      <TripEditForm trip={trip} />
      <button onClick={handleDelete}>Delete Trip</button>
      <AttendeeContainer trip={trip} currentUser={currentUser} />
      <Itineraries trip={trip} currentUser={currentUser} />
    </>
  );
}
