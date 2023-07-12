import { useEffect, useState } from "react";
import { Routes, Route } from "react-router-dom";

import TripForm from "./TripForm";
import TravelLegForm from "./TravelLegForm";
import AttendeeForm from "./AttendeeForm";
import Signup from "./Signup";
import Login from "./Login";

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
      <Home />
      <Trip /> */}
      <TripForm />
      <TravelLegForm />
      <AttendeeForm />
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
        <Route
          path="/signup"
          element={
            <Signup
              updateCurrentUser={updateCurrentUser}
              currentUser={currentUser}
            />
          }
        />
      </Routes>
    </>
  );
}
