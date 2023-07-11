from flask import Blueprint, make_response, request, session
from flask_restful import Resource
from config import db
from models import User
from schema import UserSchema


signup_bp = Blueprint("signup", __name__, url_prefix="/signup")


class SignupBP(Resource):
    def post(self):
        try:
            data = request.get_json()

            username = data.get("username")
            password = data.get("password")

            if User.query.filter(User.username == username).first():
                return make_response({"error": "Username must be unique"}, 400)

            new_user = User(username=username, public_acct=True)
            new_user.password_hash = password

            db.session.add(new_user)
            db.session.commit()

            session["user_id"] = new_user.id

            return make_response(UserSchema.dump(new_user), 201)
        except Exception as e:
            return make_response({"error": [str(e)]}, 422)