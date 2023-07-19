import React from "react";
import Task from "./Task";
import TaskFrom from "./TaskForm";

export default function TaskContainer({ trip, handleTaskAdd }) {
  return (
    <>
      <h4>Tasks:</h4>
      {trip.tasks?.map((task) => (
        <Task key={task.id} task={task} />
      ))}
      <TaskFrom trip={trip} handleTaskAdd={handleTaskAdd} />
    </>
  );
}