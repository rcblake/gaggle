from flask import Blueprint, make_response, request
from flask_restful import Api, Resource
from models import UserTask
from schema import UserTaskSchema
from config import db


user_task_bp = Blueprint("user_task", __name__, url_prefix="/user-tasks")
api = Api(user_task_bp)

user_tasks_schema = UserTaskSchema(many=True)
user_task_schema = UserTaskSchema()


class UserTaskResource(Resource):
    def get(self):
        user_tasks = UserTask.query.all()
        serialized_user_tasks = user_tasks_schema.dump(user_tasks)
        return make_response(serialized_user_tasks, 200)

    def post(self):
        user_task_data = request.get_json()
        user_task = user_task_schema.load(user_task_data)
        db.session.add(user_task)
        db.session.commit()
        return make_response(user_task_schema.dump(user_task), 201)

    def get(self, user_task_id):
        user_task = UserTask.query.get(user_task_id)
        if not user_task:
            return make_response("User task not found", 404)
        serialized_user_task = user_task_schema.dump(user_task)
        return make_response(serialized_user_task, 200)

    def patch(self, user_task_id):
        user_task = UserTask.query.get(user_task_id)
        if not user_task:
            return make_response("User task not found", 404)
        user_task_data = request.get_json()
        user_task.name = user_task_data.get("name", user_task.name)
        # Update other fields as needed
        db.session.commit()
        return make_response(user_task_schema.dump(user_task), 200)

    def delete(self, user_task_id):
        user_task = UserTask.query.get(user_task_id)
        if not user_task:
            return make_response("User task not found", 404)
        db.session.delete(user_task)
        db.session.commit()
        return make_response("User task deleted successfully", 204)
