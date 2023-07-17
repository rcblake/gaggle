import React from "react";
import { useForm } from "react-hook-form";

export default function AttendeeForm({ trip }) {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm();

  const onSubmit = async (data) => {
    try {
      const getResponse = await fetch("/users?email=" + data.email);
      const users = await getResponse.json();
      debugger;
      if (users.length > 0) {
        const user = users[0];
        debugger;
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
          console.log("User data successfully posted to '/trip_users'.");
        } else {
          console.error("Failed to post user data to '/trip_users'.");
        }
      } else {
        console.log("User with the provided email does not exist.");
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
