from flask import Blueprint, make_response, request
from config import db
from flask_restful import Resource
from models import TripUser
from schema import TripUserSchema
from sqlalchemy import and_


trip_user_bp = Blueprint("trip_user", __name__, url_prefix="/trip_users")

trip_users_schema = TripUserSchema(many=True)
trip_user_schema = TripUserSchema()


class TripUserBP(Resource):
    def get(self, trip_user_id=None):
        if trip_user_id:
            trip_user = TripUser.query.get(trip_user_id)
            if not trip_user:
                return make_response("Trip user not found", 404)
            trip_user = trip_user_schema.dump(trip_user)
            return make_response(trip_user, 200)
        else:
            trip_users = TripUser.query.all()
            trip_users = trip_users_schema.dump(trip_users)
            return make_response(trip_users, 200)

    def post(self):
        trip_user_data = request.get_json()
        t_id = trip_user_data.get("trip_id")
        u_id = trip_user_data.get("user_id")
        trip_user = trip_user_schema.load(trip_user_data, session=db.session)
        if TripUser.query.filter(
            and_(TripUser.trip_id == t_id, TripUser.user_id == u_id)
        ).first():
            return make_response({"error": "User already on Trip"}, 400)
        db.session.add(trip_user)
        db.session.commit()
        return make_response(trip_user_schema.dump(trip_user), 201)

    def patch(self, trip_user_id):
        trip_user = TripUser.query.get(trip_user_id)
        if not trip_user:
            return make_response("Trip user not found", 404)
        trip_user_data = request.get_json()
        trip_user.name = trip_user_data.get("name", trip_user.name)
        # Update other fields as needed
        db.session.commit()
        return make_response(trip_user_schema.dump(trip_user), 200)

    def delete(self, trip_user_id):
        trip_user = TripUser.query.get(trip_user_id)
        if not trip_user:
            return make_response("Trip user not found", 404)
        db.session.delete(trip_user)
        db.session.commit()
        return make_response("Trip user deleted successfully", 204)
