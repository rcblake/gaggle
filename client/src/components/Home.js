import React from "react";

import TripCard from "./TripCard";
import { useNavigate, Link } from "react-router-dom";

export default function Home({ currentUser }) {
  const navigate = useNavigate();
  const trips = currentUser?.trips;

  const handleAddClick = (e) => {
    const id = e.target.id;
    navigate("/trip_form", { id });
  };

  return (
    <>
      {currentUser ? (
        <button onClick={handleAddClick}>Plan a trip</button>
      ) : (
        <>
          <Link to="/login">
            <button>Log In</button>
          </Link>
          <Link to="/signup">
            <button>Sign Up</button>
          </Link>
        </>
      )}
      {/* <div>
        {trips.map((trip) => (
          <TripCard key={trip.id} trip={trip} />
        ))}
      </div> */}
    </>
  );
}
