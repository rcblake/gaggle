import { useEffect, useState } from "react";
import { Routes, Route, Navigate } from "react-router-dom";
import { UserContext } from "./UserContext";
import { ThemeProvider, Typography } from "@mui/material";
import { theme } from "./style";

import TripForm from "./TripForm";
import Signup from "./Signup";
import Login from "./Login";
import Home from "./Home";
import Trip from "./Trip";
import Logout from "./Logout";
import { Link, useNavigate } from "react-router-dom";

import { Button } from "@mui/material";

export default function App() {
  const [currentUser, setCurrentUser] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    fetch("/api/v1/check_session").then((res) => {
      if (res.ok) {
        res.json().then(setCurrentUser);
      }
    });
  }, []);

  const updateCurrentUser = (updated_user) => {
    setCurrentUser(updated_user);
  };

  const logout = () => {
    fetch("/api/v1/logout", {
      method: "DELETE",
    }).then((res) => {
      if (res.ok) {
        setCurrentUser(null);
        navigate("/logout");
      }
    });
  };

  return (
    <ThemeProvider theme={theme}>
      <UserContext.Provider value={currentUser}>
        {/* <AppBar />
      
      */}
        <Typography variant="h4">
          currentUser: {currentUser?.email || null}
          {currentUser?.name}
        </Typography>
        {currentUser ? (
          <>
            <Link to="/">
              <Button>Home</Button>
            </Link>
            <Button onClick={logout}>Log Out</Button>
          </>
        ) : (
          <>
            <Link to="/login">
              <Button>Log In</Button>
            </Link>
            <Link to="/signup">
              <Button>Sign Up</Button>
            </Link>
          </>
        )}

        <Routes>
          <Route
            path="/login"
            element={<Login updateCurrentUser={updateCurrentUser} />}
          />
          <Route
            path="/trips/:id"
            element={<Trip updateCurrentUser={updateCurrentUser} />}
          />
          <Route path="/logout" element={<Logout />} />

          <Route
            path="/signup"
            element={<Signup updateCurrentUser={updateCurrentUser} />}
          />
          <Route path="/trip_form" element={<TripForm />} />
          <Route path="/home" element={currentUser ? <Home /> : null} />
          <Route
            path="/"
            element={<Navigate to={currentUser ? "/home" : "/login"} />}
          />
        </Routes>
      </UserContext.Provider>
    </ThemeProvider>
  );
}
