import { useState } from "react";
import { useForm } from "react-hook-form";

import {
  Checkbox,
  Button,
  TextField,
  Dialog,
  DialogActions,
  DialogContent,
  DialogContentText,
  DialogTitle,
  FormGroup,
} from "@mui/material";
import IconButton from "@mui/material/IconButton";
import AddIcon from "@mui/icons-material/Add";
import Tooltip from "@mui/material/Tooltip";

export default function TaskFrom({ trip, handleTaskAdd }) {
  const [open, setOpen] = useState(false);

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  const {
    register,
    handleSubmit,
    reset,
    formState: { errors },
  } = useForm();

  const onSubmit = async (data) => {
    const costValue = parseFloat(data.cost);
    try {
      const newTask = {
        trip: {
          id: trip.id,
        },
        title: data.title,
        note: data.note,
        link: data.link,
        cost: costValue,
        optional: data.optional,
        // everyone: data.everyone,
      };
      console.log(newTask);
      const postResponse = await fetch("/tasks", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(newTask),
      });
      if (postResponse.ok) {
        postResponse.json().then(handleTaskAdd(newTask));
        console.log("Task added to trip tasks");
        reset();
      } else {
        console.log("Trip task failed");
      }
    } catch (error) {
      console.error("error while processing");
    }
  };

  return (
    <div>
      <Tooltip title="Add" onClick={handleClickOpen}>
        <IconButton>
          <AddIcon /> New Task
        </IconButton>
      </Tooltip>
      <Dialog open={open} onClose={handleClose}>
        <DialogTitle>New Task</DialogTitle>
        <DialogContent component="form">
          <TextField
            label="Title"
            type="text"
            name="title"
            {...register("title", {
              required: "name your task",
            })}
          />
          <TextField
            label="Note"
            type="text"
            name="note"
            {...register("note", { required: "What needs to be done?" })}
          />
          {errors.note && <p className="errorMsg">{errors.note.message}</p>}
          <TextField
            label="Link"
            type="text"
            name="link"
            {...register("link", {})}
          />
          <TextField
            label="Cost"
            type="float"
            name="cost"
            {...register("cost", {})}
          />
          <FormGroup>
            <Checkbox
              label="Optional?"
              type="checkbox"
              name="optional"
              {...register("optional", { defaultChecked: true })}
            />
            <Checkbox
              label="Everyone?"
              type="checkbox"
              name="everyone"
              {...register("optional", { defaultChecked: false })}
            />
          </FormGroup>
          <TextField type="submit" />
        </DialogContent>
      </Dialog>
    </div>
  );
}
