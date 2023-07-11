from flask import Blueprint, make_response, request
from flask_restful import Api, Resource
from models import Event
from schema import EventSchema
from config import db


event_bp = Blueprint("event", __name__, url_prefix="/events")
api = Api(event_bp)

events_schema = EventSchema(many=True)
event_schema = EventSchema()


class EventBP(Resource):
    def get(self, event_id=None):
        if event_id:
            event = Event.query.get(event_id)
            if not event:
                return make_response("Event not found", 404)
            event = event_schema.dump(event)
            return make_response(event, 200)
        else:
            events = Event.query.all()
            events = events_schema.dump(events)
            return make_response(events, 200)

    def post(self):
        event_data = request.get_json()
        event = event_schema.load(event_data)
        db.session.add(event)
        db.session.commit()
        return make_response(event_schema.dump(event), 201)

    def patch(self, event_id):
        event = Event.query.get(event_id)
        if not event:
            return make_response("Event not found", 404)
        event_data = request.get_json()
        event.name = event_data.get("name", event.name)
        # Update other fields as needed
        db.session.commit()
        return make_response(event_schema.dump(event), 200)

    def delete(self, event_id):
        event = Event.query.get(event_id)
        if not event:
            return make_response("Event not found", 404)
        db.session.delete(event)
        db.session.commit()
        return make_response("Event deleted successfully", 204)
