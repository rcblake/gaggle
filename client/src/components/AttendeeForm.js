import React from "react";
import { useForm } from "react-hook-form";

export default function AttendeeForm({ trip, handleAttendeeAdd }) {
  const {
    register,
    handleSubmit,
    reset,
    formState: { errors },
  } = useForm();
  const onSubmit = async (data) => {
    try {
      const getResponse = await fetch("/users");
      const users = await getResponse.json();
      const user = users.find((u) => u.email === data.email);
      if (user) {
        const newTripUser = {
          user_id: user.id,
          trip_id: trip.id,
          is_admin: false,
        };
        const postResponse = await fetch("/trip_users", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(newTripUser),
        });
        if (postResponse.ok) {
          handleAttendeeAdd(user);
          reset();
          console.log("User data successfully posted to '/trip_users'.");
        } else {
          console.error("Failed to post user data to '/trip_users'.");
          alert("User already on Trip");
        }
      } else {
        console.error("User does not exist");
        alert(
          "That user is not on Gaggle yet. Invite them to use Gaggle today!"
        );
      }
    } catch (error) {
      console.error("An error occurred while processing the request:", error);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit(onSubmit)}>
        <label>email:</label>
        <input
          type="email"
          name="email"
          {...register("email", {
            required: "email is required",
          })}
        />
        {errors.email && <p className="errorMsg">{errors.email.message}</p>}
        <input type="submit" />
      </form>
    </div>
  );
}
