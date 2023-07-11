import React, { useEffect, useState } from "react";
import { Switch, Route } from "react-router-dom";

import TripForm from "./TripForm";
import TravelLegForm from "./TravelLegForm";
import AttendeeForm from "./AttendeeForm";

function App() {
  return (
    <>
      {/* <AppBar />
      <Home />
      <Trip /> */}
      <TripForm />
      <TravelLegForm />
      <AttendeeForm />
    </>
  );
}

export default App;
