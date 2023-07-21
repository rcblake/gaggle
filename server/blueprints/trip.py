from flask import Blueprint, make_response, request
from config import db, ValidationError
from flask_restful import Api, Resource
from models import Trip
from schema import TripSchema

trip_bp = Blueprint("trip", __name__, url_prefix="/api/v1/trips")
api = Api(trip_bp)

trips_schema = TripSchema(many=True)
trip_schema = TripSchema()


class TripBP(Resource):
    def get(self, trip_id=None):
        if trip_id:
            trip = Trip.query.get(trip_id)
            if not trip:
                return make_response("Trip not found", 404)
            trip = trip_schema.dump(trip)
            return make_response(trip, 200)
        else:
            trips = Trip.query.all()
            trips = trips_schema.dump(trips)
            return make_response(trips, 200)

    def post(self):
        trip_data = request.get_json()

        try:
            trip = trip_schema.load(trip_data, session=db.session)
            db.session.add(trip)
            db.session.commit()
            return make_response(trip_schema.dump(trip), 201)
        except ValidationError as e:
            return make_response({"errors": e.messages}, 400)
        except Exception as e:
            return make_response(
                {"error": "An error occurred while processing the request"}, 500
            )

    def patch(self, trip_id):
        trip = Trip.query.get(trip_id)
        if not trip:
            return make_response("Trip not found", 404)

        trip_data = request.get_json()
        try:
            trip = trip_schema.load(
                trip_data, instance=trip, partial=True, session=db.session
            )
            db.session.commit()
            return make_response(trip_schema.dump(trip), 200)
        except ValidationError as e:
            return make_response({"errors": e.messages}, 400)
        except Exception as e:
            return make_response(
                {"error": "An error occurred while processing the request"}, 500
            )

    def delete(self, trip_id):
        trip = Trip.query.get(trip_id)
        if not trip:
            return make_response("Trip not found", 404)
        db.session.delete(trip)
        db.session.commit()
        return make_response("Trip deleted successfully", 204)
