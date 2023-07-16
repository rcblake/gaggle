import { useEffect, useState } from "react";
import { Routes, Route } from "react-router-dom";

import TripForm from "./TripForm";
import Signup from "./Signup";
import Login from "./Login";
import Home from "./Home";
import Trip from "./Trip";
import Logout from "./Logout";
import { Link, useNavigate } from "react-router-dom";

export default function App() {
  const [currentUser, setCurrentUser] = useState(null);
  const navigate = useNavigate();

  // useEffect(() => {
  //   fetch("/check_session").then((res) => {
  //     if (res.ok) {
  //       res.json().then(setCurrentUser);
  //     }
  //   });
  // }, []);

  useEffect(
    () =>
      fetch("users/1").then((res) => {
        if (res.ok) {
          res.json().then(setCurrentUser);
        }
      }),
    []
  );

  const updateCurrentUser = (updated_user) => {
    setCurrentUser(updated_user);
  };

  const logout = () => {
    fetch("/logout", {
      method: "DELETE",
    }).then((res) => {
      if (res.ok) {
        setCurrentUser(null);
        navigate("/logout");
      }
    });
  };
  return (
    <>
      {/* <AppBar />
      
      */}
      <h4>currentUser: {currentUser?.email || null}</h4>
      <Link to="/login">
        <button>Log In</button>
      </Link>
      <Link to="/signup">
        <button>Sign Up</button>
      </Link>

      <button onClick={logout}>Log Out</button>

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
        <Route path="/logout" element={<Logout />} />

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
