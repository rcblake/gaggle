import { useState, useContext } from "react";
import { useForm } from "react-hook-form";
import { UserContext } from "./UserContext";

import {
  Checkbox,
  Button,
  Select,
  MenuItem,
  TextField,
  Dialog,
  DialogActions,
  DialogContent,
  DialogContentText,
  DialogTitle,
  FormGroup,
} from "@mui/material";

export default function TravelLegForm({ trip, handleTravelLegAdd }) {
  const currentUser = useContext(UserContext);
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
    try {
      const newTravelLeg = {
        trip: {
          id: trip.id,
        },
        user: {
          id: currentUser.id,
          name: currentUser.name,
        },
        travel_type: data.travelDirection,
        departure_time: data.departureTime,
        arrival_time: data.arrivalTime,
        flight_number: data.note,
      };
      console.log(newTravelLeg);
      const postResponse = await fetch("/api/v1/travel_legs", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(newTravelLeg),
      });
      if (postResponse.ok) {
        handleTravelLegAdd(newTravelLeg);
        console.log("Travel leg successfully posted to /travel_legs");
        reset();
      } else {
        console.log("Failed to post to /travel_legs");
      }
    } catch (error) {
      console.error("error while processing");
    }
  };

  return (
    <div>
      <Button variant="outlined" onClick={handleClickOpen}>
        Add your Travel
      </Button>
      <Dialog open={open} onClose={handleClose}>
        <DialogTitle>New Travel leg</DialogTitle>
        <DialogContent onSubmit={handleSubmit(onSubmit)}>
          <Select
            label="Direction"
            value="travelDdirection"
            name="travelDirection"
            {...register("travelDirection", {
              required: "Select travel direction",
            })}
          >
            <MenuItem value="Depart">Depart</MenuItem>
            <MenuItem value="Return">Return</MenuItem>
          </Select>
          <TextField
            label="Departure Date/Time"
            type="datetime-local"
            name="departureTime"
            {...register("departureTime", {
              required: "Departure Time is required",
            })}
          />
          {errors.departureTime && (
            <p className="">{errors.departureTime.message}</p>
          )}
          <TextField
            label="Arrival Date/Time"
            type="datetime-local"
            name="arrivalTime"
            {...register("arrivalTime", {
              required: "Arrival Time is required",
            })}
          />
          {errors.arrivalTime && (
            <p className="">{errors.arrivalTime.message}</p>
          )}
          <TextField
            label="Note/Flight #"
            type="text"
            name="note"
            {...register("note", {})}
          />
          {errors.note && <p className="errorMsg">{errors.note.message}</p>}
          <TextField type="submit" />
        </DialogContent>
      </Dialog>
    </div>
  );
}
