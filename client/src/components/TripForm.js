import { useContext, useState } from "react";
import { useForm } from "react-hook-form";
import { useNavigate } from "react-router";

import {
  Typography,
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
import { UserContext } from "./UserContext";

export default function TripForm({ handleAttendeeAdd }) {
  const [open, setOpen] = useState(false);
  const currentUser = useContext(UserContext);

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  const {
    register,
    handleSubmit,
    getValues,
    reset,
    formState: { errors },
  } = useForm();
  const navigate = useNavigate();

  const onSubmit = async (data) => {
    try {
      console.log(data);
      const response = await fetch("/api/v1/trips", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });

      if (response.ok) {
        const trip = await response.json();
        newTripUser(trip);
      } else {
        console.log("Error creating trip");
      }
    } catch (error) {
      console.log("Error creating trip", error);
    }
  };

  const newTripUser = async (trip) => {
    const newTripUser = {
      user_id: currentUser.id,
      trip_id: trip.id,
      is_admin: true,
    };
    const postResponse = await fetch("/trip_users", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(newTripUser),
    });
    if (postResponse.ok) {
      navigate(`/trips/${trip.id}`);
    } else {
      alert("User already on Trip");
    }
  };

  return (
    <div>
      <Tooltip title="newTrip" onClick={handleClickOpen}>
        <IconButton>
          <AddIcon /> Plan a Trip
        </IconButton>
      </Tooltip>
      <Dialog open={open} onClose={handleClose}>
        <DialogTitle>Your next Trip</DialogTitle>
        <form onSubmit={handleSubmit(onSubmit)}>
          <DialogContent>
            <FormGroup>
              <label>Trip Name:</label>
              <TextField
                type="text"
                name="name"
                {...register("name", {
                  required: "Name is required",
                })}
              />
              {errors.name && <p className="errorMsg">{errors.name.message}</p>}
              <Typography variant="body1">Location: </Typography>
              <TextField
                type="text"
                name="location"
                {...register("location", {})}
              />
              <label>Start Date:</label>
              <TextField
                type="date"
                name="start_date"
                {...register("start_date", {
                  required: "Start Date is required",
                })}
              />
              {errors.start_date && (
                <p className="errorMsg">{errors.start_date.message}</p>
              )}
              <label>End Date:</label>
              <TextField
                type="date"
                name="end_date"
                {...register("end_date", {
                  required: "End Date is required",
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
