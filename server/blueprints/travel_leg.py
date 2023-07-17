from flask import Blueprint, make_response, request
from flask_restful import Api, Resource
from models import TravelLeg
from schema import TravelLegSchema
from config import db


travel_leg_bp = Blueprint("travel_leg", __name__, url_prefix="/travel_legs")

travel_legs_schema = TravelLegSchema(many=True)
travel_leg_schema = TravelLegSchema()


class TravelLegBP(Resource):
    def get(self, travel_leg_id=None):
        if travel_leg_id:
            travel_leg = TravelLeg.query.get(travel_leg_id)
            if not travel_leg:
                return make_response("Travel leg not found", 404)
            travel_leg = travel_leg_schema.dump(travel_leg)
            return make_response(travel_leg, 200)
        else:
            travel_legs = TravelLeg.query.all()
            travel_legs = travel_legs_schema.dump(travel_legs)
            return make_response(travel_legs, 200)

    def post(self):
        travel_leg_data = request.get_json()
        travel_leg = travel_leg_schema.load(travel_leg_data, session=db.session)
        db.session.add(travel_leg)
        db.session.commit()
        return make_response(travel_leg_schema.dump(travel_leg), 201)

    def patch(self, travel_leg_id):
        travel_leg = TravelLeg.query.get(travel_leg_id)
        if not travel_leg:
            return make_response("Travel leg not found", 404)
        travel_leg_data = request.get_json()
        travel_leg.name = travel_leg_data.get("name", travel_leg.name)
        # Update other fields as needed
        db.session.commit()
        return make_response(travel_leg_schema.dump(travel_leg), 200)

    def delete(self, travel_leg_id):
        travel_leg = TravelLeg.query.get(travel_leg_id)
        if not travel_leg:
            return make_response("Travel leg not found", 404)
        db.session.delete(travel_leg)
        db.session.commit()
        return make_response("Travel leg deleted successfully", 204)
