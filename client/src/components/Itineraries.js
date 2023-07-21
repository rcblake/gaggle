import createData from "react";

import TravelLegForm from "./TravelLegForm";
import TravelLeg from "./TravelLeg";

import { TableFooter, Typography, Box } from "@mui/material";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";

export default function Itineraries({ trip, handleTravelLegAdd }) {
  function createData(userName, direction, departure, arrival, note, id) {
    return { userName, direction, departure, arrival, note, id };
  }

  const dateTimeFormat = (dateTime) => {
    const formatter = new Intl.DateTimeFormat("en-US", {
      month: "2-digit",
      day: "2-digit",
      year: "2-digit",
      hour: "2-digit",
      minute: "2-digit",
      hour12: true,
    });

    const formattedDateTime = formatter.format(new Date(dateTime));
    const centerSymbol = " @ ";
    return formattedDateTime.replace(" ", centerSymbol);
  };

  const rows = trip.travel_legs?.map((travel_leg) =>
    createData(
      travel_leg.user.name,
      travel_leg.travel_type,
      dateTimeFormat(travel_leg.departure_time),
      dateTimeFormat(travel_leg.arrival_time),
      travel_leg.flight_number,
      travel_leg.id
    )
  );
  return (
    <TableContainer component={Paper}>
      <Box display="flex" flexDirection="row" alignItems={"center"}>
        <Typography variant="h4">travel</Typography>
        <TravelLegForm trip={trip} handleTravelLegAdd={handleTravelLegAdd} />
      </Box>
      <Table aria-label="itinerary table">
        <TableHead>
          <TableRow>
            <TableCell align="left">Traveler</TableCell>
            <TableCell align="center">Direction</TableCell>
            <TableCell align="center">Departure</TableCell>
            <TableCell align="center">Arrival</TableCell>
            <TableCell align="center">Note/Flight #</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows?.map((row) => (
            <TableRow
              key={row.id}
              sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
            >
              <TableCell align="left">{row.userName}</TableCell>
              <TableCell align="center">{row.direction}</TableCell>
              <TableCell align="center">{row.departure}</TableCell>
              <TableCell align="center">{row.arrival}</TableCell>
              <TableCell align="center">{row.note}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}
