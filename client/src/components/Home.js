import React from "react";

import { useNavigate } from "react-router-dom";
import MyTrips from "./MyTrips";

export default function Home({ currentUser }) {
  const navigate = useNavigate();

  if (!currentUser) {
    navigate("/signup");
  }

  const handleAddClick = (e) => {
    const id = e.target.id;
    navigate("/trip_form", { id });
  };

  return (
    <>
      <button onClick={handleAddClick}>Plan a trip</button>
      <MyTrips currentUser={currentUser} />
    </>
  );
}
