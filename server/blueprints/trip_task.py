from flask import Blueprint, make_response, request
from flask_restful import Api, Resource
from models import TripTask
from schema import TripTaskSchema
from config import db


trip_task_bp = Blueprint("trip_task", __name__, url_prefix="/trip_tasks")
api = Api(trip_task_bp)

trip_tasks_schema = TripTaskSchema(many=True)
trip_task_schema = TripTaskSchema()


class TripTask(Resource):
    def get(self, trip_task_id=None):
        if trip_task_id:
            trip_task = TripTask.query.get(trip_task_id)
            if not trip_task:
                return make_response("Trip task not found", 404)
            trip_task = trip_task_schema.dump(trip_task)
            return make_response(trip_task, 200)
        else:
            trip_tasks = TripTask.query.all()
            trip_tasks = trip_tasks_schema.dump(trip_tasks)
            return make_response(trip_tasks, 200)

    def post(self):
        trip_task_data = request.get_json()
        trip_task = trip_task_schema.load(trip_task_data)
        db.session.add(trip_task)
        db.session.commit()
        return make_response(trip_task_schema.dump(trip_task), 201)

    def get(self, trip_task_id):
        trip_task = TripTask.query.get(trip_task_id)
        if not trip_task:
            return make_response("Trip task not found", 404)
        trip_task = trip_task_schema.dump(trip_task)
        return make_response(trip_task, 200)

    def patch(self, trip_task_id):
        trip_task = TripTask.query.get(trip_task_id)
        if not trip_task:
            return make_response("Trip task not found", 404)
        trip_task_data = request.get_json()
        trip_task.name = trip_task_data.get("name", trip_task.name)
        # Update other fields as needed
        db.session.commit()
        return make_response(trip_task_schema.dump(trip_task), 200)

    def delete(self, trip_task_id):
        trip_task = TripTask.query.get(trip_task_id)
        if not trip_task:
            return make_response("Trip task not found", 404)
        db.session.delete(trip_task)
        db.session.commit()
        return make_response("Trip task deleted successfully", 204)
