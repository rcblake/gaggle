from flask import Blueprint, make_response, session
from flask_restful import Resource
from config import db
from models import User
from schema import UserSchema

check_session_bp = Blueprint(
    "check_session", __name__, url_prefix="/api/v1/check_session"
)


class CheckSessionBP(Resource):
    def get(self):
        if "user_id" in session:
            user_id = session["user_id"]
            user = db.session.query(User).get(user_id)
            if user:
                user_schema = UserSchema()
                user_data = user_schema.dump(user)

                return make_response(user_data, 200)
