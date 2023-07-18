import { useState, useEffect, useContext } from "react";
import AttendeeContainer from "./AttendeeContainer";
import Itineraries from "./Itineraries";
import { useNavigate, useParams } from "react-router";
import TripEditForm from "./TripEditForm";
import { UserContext } from "./UserContext";

export default function Trip() {
  const [trip, setTrip] = useState({});
  const navigate = useNavigate();
  const { id } = useParams();
  const currentUser = useContext(UserContext);

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

  const handleTripEdit = () => {
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
  };

  const handleDelete = () => {};
  return (
    <>
      {/* <TripHeader /> */}
      <h2>Trip:{trip.name}</h2>
      Edit:
      <TripEditForm trip={trip} handleTripEdit={handleTripEdit} />
      <button onClick={handleDelete}>Delete Trip</button>
      <AttendeeContainer trip={trip} handleAttendeeAdd={handleAttendeeAdd} />
      <Itineraries trip={trip} handleTravelLegAdd={handleTravelLegAdd} />
    </>
  );
}
