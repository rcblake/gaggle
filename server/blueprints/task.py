from flask import Blueprint, make_response, request
from flask_restful import Api, Resource
from models import Task
from schema import TaskSchema
from config import db, ValidationError


task_bp = Blueprint("task", __name__, url_prefix="/tasks")
api = Api(task_bp)

tasks_schema = TaskSchema(many=True)
task_schema = TaskSchema()


class TaskBP(Resource):
    def get(self, task_id=None):
        if task_id:
            task = Task.query.get(task_id)
            if not task:
                return make_response("Trip task not found", 404)
            task = task_schema.dump(task)
            return make_response(task, 200)
        else:
            tasks = Task.query.all()
            tasks = tasks_schema.dump(tasks)
            return make_response(tasks, 200)

    def post(self):
        task_data = request.get_json()
        try:
            task = task_schema.load(task_data, session=db.session)
            db.session.add(task)
            db.session.commit()
            return make_response(task_schema.dump(task), 201)
        except ValidationError as e:
            return make_response({"errors": e.messages}, 400)
        except Exception as e:
            return make_response(
                {"error": "An error occurred while processing the request"}, 500
            )

    def patch(self, task_id):
        task = Task.query.get(task_id)
        if not task:
            return make_response("Trip task not found", 404)
        task_data = request.get_json()
        task.name = task_data.get("name", task.name)
        # Update other fields as needed
        db.session.commit()
        return make_response(task_schema.dump(task), 200)

    def delete(self, task_id):
        task = Task.query.get(task_id)
        if not task:
            return make_response("Trip task not found", 404)
        db.session.delete(task)
        db.session.commit()
        return make_response("Trip task deleted successfully", 204)
