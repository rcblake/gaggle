import { useEffect, useState } from "react";
import { Routes, Route } from "react-router-dom";

import TripForm from "./TripForm";
import TravelLegForm from "./TravelLegForm";
import AttendeeForm from "./AttendeeForm";
import Signup from "./Signup";
import Login from "./Login";
import Home from "./Home";
import Trip from "./Trip";
import { Link } from "react-router-dom";

export default function App() {
  const [currentUser, setCurrentUser] = useState(null);

  useEffect(() => {
    fetch("/check_session").then((res) => {
      if (res.ok) {
        res.json().then(setCurrentUser);
      }
    });
  }, []);

  const updateCurrentUser = (updated_user) => {
    setCurrentUser(updated_user);
  };
  return (
    <>
      {/* <AppBar />
      
      */}
      <Link to="/login">
        <button>Log In</button>
      </Link>
      <Link to="/signup">
        <button>Sign Up</button>
      </Link>
      <Link to="/logout">
        <button>Log Out</button>
      </Link>
      <Routes>
        <Route
          path="/login"
          element={
            <Login
              updateCurrentUser={updateCurrentUser}
              currentUser={currentUser}
            />
          }
        />
        <Route path="/trips/:id" element={<Trip currentUser={currentUser} />} />

        <Route
          path="/signup"
          element={
            <Signup
              updateCurrentUser={updateCurrentUser}
              currentUser={currentUser}
            />
          }
        />
        <Route
          path="/trip_form"
          element={<TripForm currentUser={currentUser} />}
        />
        <Route path="/" element={<Home currentUser={currentUser} />} />
      </Routes>
    </>
  );
}
