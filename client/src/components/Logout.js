import React from "react";
import { Paper, Box, Typography } from "@mui/material";

export default function Logout() {
  return (
    <Paper sx={{ backgroundColor: "#C7623B", height: "100vh" }}>
      <Box
        sx={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          backgroundColor: "#C7623B",
          paddingTop: 20,
        }}
      >
        <Typography variant="h3">Logged out successfully</Typography>
      </Box>
    </Paper>
  );
}
