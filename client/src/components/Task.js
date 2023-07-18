import React from "react";

export default function Task({ task }) {
  return (
    <p>
      title:{task.title} , note:{task.note} , link:{task.link} , cost:
      {task.cost} , optional?{task.optional}
    </p>
  );
}
