from flask import Blueprint, make_response, session
from flask_restful import Resource
from config import db
from models import User
from schema import UserSchema

check_session_bp = Blueprint("check_session", __name__, url_prefix="/check_session")


class CheckSessionBP(Resource):
    def get(self):
        if id := session.get("user_id"):
            if user := db.session.get(User, id):
                return make_response(UserSchema.dump(user), 200)
