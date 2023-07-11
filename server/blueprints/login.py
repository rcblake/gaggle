from flask import Blueprint, make_response, request, session
from flask_restful import Resource
from models import User
from schema import UserSchema

login_bp = Blueprint("login", __name__, url_prefix="/login")


class Login(Resource):
    def post(self):
        try:
            data = request.get_json()

            username = data.get("username")
            password = data.get("password")
            if user := User.query.filter(User.username == username).first():
                if user.authenticate(password):
                    session["user_id"] = user.id
                    return make_response(UserSchema.dump(user), 200)
            return make_response({"error": "Invalid credentials"}, 401)
        except:
            return make_response({"error": "Invalid credentials"}, 401)