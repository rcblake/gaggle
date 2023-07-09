from flask import Blueprint, make_response, request
from config import db
from flask_restful import Resource
from models import Trip
from schema import TripSchema

trip_bp = Blueprint("trip", __name__, url_prefix="/trips")

trips_schema = TripSchema(many=True)
trip_schema = TripSchema()


class TripResource(Resource):
    def get(self, trip_id=None):
        if trip_id:
            trip = Trip.query.get(trip_id)
            if not trip:
                return make_response("Trip not found", 404)
            serialized_trips = trip_schema.dump(trip)
            return make_response(serialized_trips, 200)
        else:
            trips = Trip.query.all()
            serialized_trips = trips_schema.dump(trips)
            return make_response(serialized_trips, 200)

    def post(self):
        trip_data = request.get_json()
        trip = trip_schema.load(trip_data)
        db.session.add(trip)
        db.session.commit()
        return make_response(trip_schema.dump(trip), 201)

    def patch(self, trip_id):
        trip = Trip.query.get(trip_id)
        if not trip:
            return make_response("Trip not found", 404)
        trip_data = request.get_json()
        trip.name = trip_data.get("name", trip.name)
        #! Update other fields
        db.session.commit()
        return make_response(trip_schema.dump(trip), 200)

    def delete(self, trip_id):
        trip = Trip.query.get(trip_id)
        if not trip:
            return make_response("Trip not found", 404)
        db.session.delete(trip)
        db.session.commit()
        return make_response("Trip deleted successfully", 204)
