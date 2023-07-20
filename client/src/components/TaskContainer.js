import createData from "react";
import TaskForm from "./TaskForm";

import { TableFooter, Typography, Box } from "@mui/material";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import DeleteIcon from "@mui/icons-material/Delete";
import IconButton from "@mui/material/IconButton";
import AddIcon from "@mui/icons-material/Add";
import Tooltip from "@mui/material/Tooltip";

export default function TaskContainer({ trip, handleTaskAdd }) {
  function createData(title, note, link, cost, optional, everyone) {
    return { title, note, link, cost, optional, everyone };
  }

  const rows = trip.tasks?.map((task) =>
    createData(
      task.title,
      task.note,
      task.link,
      task.cost,
      task.optional,
      task.everyone
    )
  );

  return (
    <TableContainer component={Paper}>
      <Box display="flex" flexDirection="row" alignItems={"center"}>
        <Typography variant="h4">tasks</Typography>
        <TaskForm trip={trip} handleTaskAdd={handleTaskAdd} />
      </Box>

      <Table aria-label="tasks table">
        <TableHead>
          <TableRow>
            <TableCell align="left">Task</TableCell>
            <TableCell align="center">Description</TableCell>
            <TableCell align="center">Link</TableCell>
            <TableCell align="center">Cost</TableCell>
            <TableCell align="center">Optional?</TableCell>
            <TableCell align="center">Everyone?</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows?.map((row) => (
            <TableRow
              key={row.Task}
              sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
            >
              <TableCell align="center">{row.title}</TableCell>
              <TableCell align="center">{row.note}</TableCell>
              <TableCell align="center">{row.link}</TableCell>
              <TableCell align="center">{row.cost}</TableCell>
              <TableCell align="center">{row.optional}</TableCell>
              <TableCell align="center">{row.everyone}</TableCell>
              <Tooltip title="Delete">
                <IconButton>
                  <DeleteIcon />
                </IconButton>
              </Tooltip>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}
