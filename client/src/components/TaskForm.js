import { useContext } from "react";
import { useForm } from "react-hook-form";
import { UserContext } from "./UserContext";

export default function TaskFrom({ trip, handleTaskAdd }) {
  const currentUser = useContext(UserContext);
  const {
    register,
    handleSubmit,
    reset,
    formState: { errors },
  } = useForm();

  const onSubmit = async (data) => {
    try {
      const newTask = {
        title: data.title,
        note: data.note,
        link: data.link,
        cost: data.cost,
        optional: data.optional,
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
        handleTaskAdd(newTask);
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
      <form onSubmit={handleSubmit(onSubmit)}>
        <label>Title</label>
        <input
          type="text"
          name="title"
          {...register("title", {
            required: "name your task",
          })}
        />
        <label>Note</label>
        <input
          type="text"
          name="note"
          {...register("note", { required: "What needs to be done?" })}
        />
        {errors.note && <p className="errorMsg">{errors.note.message}</p>}
        <label>Link:</label>
        <input type="text" name="link" {...register("link", {})} />
        <label>Cost:</label>
        <input type="float" name="cost" {...register("cost", {})} />
        <label>Optional?</label>
        <input
          type="checkbox"
          name="optional"
          {...register("optional", { defaultChecked: false })}
        />
        <input type="submit" />
      </form>
    </div>
  );
}
