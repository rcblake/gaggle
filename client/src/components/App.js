import React, { useEffect, useState } from "react";
import { Switch, Route } from "react-router-dom";

function App() {
  return (
    <>
      <AppBar />
      <Home />
      <Trip />
    </>
  );
}

export default App;
