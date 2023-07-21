import React from "react";

import { useNavigate } from "react-router-dom";
import MyTrips from "./MyTrips";
import TripForm from "./TripForm";

export default function Home() {
  const navigate = useNavigate();

  const handleAddClick = (e) => {
    const id = e.target.id;
    navigate("/trip_form", { id });
  };

  return (
    <>
      <TripForm />
      <MyTrips />
    </>
  );
}
