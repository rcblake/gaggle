from flask import Blueprint, make_response, request
from flask_restful import Api, Resource
from models import Lodging
from schema import LodgingSchema
from config import db

lodging_bp = Blueprint("lodging", __name__, url_prefix="/lodgings")
api = Api(lodging_bp)

lodgings_schema = LodgingSchema(many=True)
lodging_schema = LodgingSchema()


class LodgingBP(Resource):
    def get(self, lodging_id=None):
        if lodging_id:
            lodging = Lodging.query.get(lodging_id)
            if not lodging:
                return make_response("Lodging not found", 404)
            lodging = lodging_schema.dump(lodging)
            return make_response(lodging, 200)
        else:
            lodgings = Lodging.query.all()
            lodgings = lodgings_schema.dump(lodgings)
            return make_response(lodgings, 200)

    def post(self):
        lodging_data = request.get_json()
        lodging = lodging_schema.load(lodging_data)
        db.session.add(lodging)
        db.session.commit()
        return make_response(lodging_schema.dump(lodging), 201)

    def patch(self, lodging_id):
        lodging = Lodging.query.get(lodging_id)
        if not lodging:
            return make_response("Lodging not found", 404)
        lodging_data = request.get_json()
        lodging.name = lodging_data.get("name", lodging.name)
        # Update other fields as needed
        db.session.commit()
        return make_response(lodging_schema.dump(lodging), 200)

    def delete(self, lodging_id):
        lodging = Lodging.query.get(lodging_id)
        if not lodging:
            return make_response("Lodging not found", 404)
        db.session.delete(lodging)
        db.session.commit()
        return make_response("Lodging deleted successfully", 204)
