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
  function createData(title, note, link, cost, optional, everyone, id) {
    return { title, note, link, cost, optional, everyone, id };
  }

  const rows = trip.tasks?.map((task) =>
    createData(
      task.title,
      task.note,
      task.link,
      task.cost,
      task.optional,
      task.everyone,
      task.id
    )
  );

  // const handleDelete = (id) => {
  //   fetch(`/task/${id}`, {
  //     method: "DELETE",
  //   });
  // };

  return (
    <TableContainer component={Paper}>
      <Box
        marginLeft={3}
        display="flex"
        flexDirection="row"
        alignItems={"center"}
      >
        <Typography variant="h4">tasks</Typography>
        <TaskForm display="flex" trip={trip} handleTaskAdd={handleTaskAdd} />
      </Box>

      <Table aria-label="tasks table">
        <TableHead>
          <TableRow>
            <TableCell align="left">Task</TableCell>
            <TableCell align="center">Description</TableCell>
            <TableCell align="center">Link</TableCell>
            <TableCell align="center">Cost</TableCell>
            {/* <TableCell align="center">Optional?</TableCell>
            <TableCell align="center">Everyone?</TableCell> */}
          </TableRow>
        </TableHead>
        <TableBody>
          {rows?.map((row) => (
            <TableRow
              key={row.id}
              sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
            >
              <TableCell align="center">{row.title}</TableCell>
              <TableCell align="center">{row.note}</TableCell>
              <TableCell align="center">{row.link}</TableCell>
              <TableCell align="center">{row.cost}</TableCell>
              {/* <TableCell align="center">{row.optional}</TableCell>
              <TableCell align="center">{row.everyone}</TableCell> */}
              {/* <TableCell>
                <Tooltip title="Delete">
                  <IconButton onClick={handleDelete(row.id)}>
                    <DeleteIcon />
                  </IconButton>
                </Tooltip>
              </TableCell> */}
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}
