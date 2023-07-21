import { useState, useEffect, useContext } from "react";
import { useNavigate, useParams } from "react-router";
import { UserContext } from "./UserContext";
import TripEditForm from "./TripEditForm";
import AttendeeContainer from "./AttendeeContainer";
import Itineraries from "./Itineraries";
import TaskContainer from "./TaskContainer";

import Alert from "@mui/material/Alert";
import Stack from "@mui/material/Stack";
import { Box } from "@mui/material";

export default function Trip({ updateCurrentUser }) {
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
          navigate("/404");
        }
      })
      .then((trip) => {
        if (trip.users.find((user) => user.email !== currentUser.email)) {
          setTrip(trip);
        } else {
          navigate("/404");
        }
      })
      .catch((err) => {
        navigate("/404");
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

  const handleTaskAdd = (newTask) =>
    setTrip((prevState) => {
      debugger;
      const obj = {
        ...(prevState = {
          tasks: [...prevState.tasks, newTask],
        }),
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
        setTrip(trip);
      })
      .catch((err) => {
        console.error(err);
      });
  };

  const handleDelete = () => {
    fetch(`/trips/${id}`, {
      method: "DELETE",
    }).then((res) => {
      if (res.ok) {
        Alert("Your trip was successfully deleted");
        updateCurrentUser(currentUser);
        navigate("/");
      } else {
        console.log("trip not deleted");
      }
    });
  };
  return (
    <>
      <Box sx={{ display: "flex", flexDirection: "row", height: 200 }}>
        <Box>
          <TripEditForm trip={trip} handleTripEdit={handleTripEdit} />
          <button onClick={handleDelete}>Delete Trip</button>
        </Box>
        <AttendeeContainer trip={trip} handleAttendeeAdd={handleAttendeeAdd} />
      </Box>
      <Itineraries trip={trip} handleTravelLegAdd={handleTravelLegAdd} />
      <TaskContainer trip={trip} handleTaskAdd={handleTaskAdd} />
    </>
  );
}
