import React from "react";
import { Paper, Box, Typography } from "@mui/material";

export default function Error404() {
  return (
    <Paper sx={{ backgroundColor: "#C7623B", height: "100vh" }}>
      <Box
        sx={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          backgroundColor: "#C7623B",
        }}
      >
        <Typography variant="h1">404</Typography>
        <Typography variant="h3">That page can not be found</Typography>
      </Box>
    </Paper>
  );
}
