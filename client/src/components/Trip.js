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

  const handleAttendeeAdd = (newAttendee) =>
    setTrip((prevState) => {
      return {
        ...prevState,
        users: [
          ...prevState.users,
          {
            user: {
              email: newAttendee.email,
              id: newAttendee.id,
              name: newAttendee.name,
            },
          },
        ],
      };
    });

  const handleTravelLegAdd = (newTravelLeg) =>
    setTrip((prevState) => {
      const obj = {
        ...prevState,
        travel_legs: [...prevState.travel_legs, newTravelLeg],
      };
      console.log(obj);
      return obj;
    });
  return (
    <>
      {/* <TripHeader /> */}
      <h2>Trip:{trip.name}</h2>
      <AttendeeContainer trip={trip} handleAttendeeAdd={handleAttendeeAdd} />
      <Itineraries
        trip={trip}
        currentUser={currentUser}
        handleTravelLegAdd={handleTravelLegAdd}
      />
    </>
  );
}
