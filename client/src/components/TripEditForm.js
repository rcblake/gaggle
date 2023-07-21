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
import EditIcon from "@mui/icons-material/Edit";
import Tooltip from "@mui/material/Tooltip";

export const dirtyValues = (dirtyFields, allValues) => {
  if (dirtyFields === true || Array.isArray(dirtyFields)) {
    return allValues;
  }

  return Object.fromEntries(
    Object.keys(dirtyFields).map((key) => [
      key,
      dirtyValues(dirtyFields[key], allValues[key]),
    ])
  );
};

export default function TripEditForm({ trip, handleTripEdit }) {
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
    formState,
    getValues,
    formState: { errors },
  } = useForm({
    mode: "onChange",
    defaultValues: {
      name: trip?.name,
      location: trip?.location,
      start_date: trip?.start_date,
      end_date: trip?.end_date,
    },
  });

  const onSubmit = async (data) => {
    debugger;
    try {
      console.log(dirtyValues(formState.dirtyFields, data));
      const tripEdit = dirtyValues(formState.dirtyFields, data);
      const response = await fetch(`/trips/${trip.id}`, {
        method: "PATCH",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(tripEdit),
      });

      if (response.ok) {
        const trip = await response.json();
        handleTripEdit();
        handleClose();
      } else {
        console.log("Error creating trip");
      }
    } catch (error) {
      console.log("Error creating trip", error);
    }
  };

  return (
    <div>
      <Tooltip title="editTrip" onClick={handleClickOpen}>
        <IconButton size="small">
          <EditIcon /> Edit Trip
        </IconButton>
      </Tooltip>
      <Dialog open={open} onClose={handleClose}>
        <DialogTitle>Edit Trip</DialogTitle>
        <form onSubmit={handleSubmit(onSubmit)}>
          <DialogContent>
            <FormGroup>
              <TextField
                defaultValue={trip.name}
                label="Trip Name"
                type="text"
                name="name"
                {...register("name", {})}
              />
              {errors.name && <p className="errorMsg">{errors.name.message}</p>}
              <TextField
                label="Location"
                defaultValue={trip.location}
                type="text"
                name="location"
                {...register("location", {})}
              />
              <TextField
                label="Start Date"
                defaultValue={trip.start_date}
                type="date"
                name="start_date"
                {...register("start_date", {})}
              />
              {errors.start_date && (
                <p className="errorMsg">{errors.start_date.message}</p>
              )}
              <TextField
                label="End Date"
                defaultValue={trip.end_date}
                type="date"
                name="end_date"
                {...register("end_date", {
                  validate: (value) => value > getValues().start_date,
                })}
              />
              {errors.end_date && (
                <p className="errorMsg">{errors.end_date.message}</p>
              )}
            </FormGroup>
          </DialogContent>
          <DialogActions>
            <Button onClick={handleClose}>Cancel</Button>
            <Button type="submit">Save</Button>
          </DialogActions>
        </form>
      </Dialog>
    </div>
  );
}
