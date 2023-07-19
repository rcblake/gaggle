from flask import Blueprint, make_response, request, session
from flask_restful import Resource
from models import User
from schema import UserSchema

login_bp = Blueprint("login", __name__, url_prefix="api/login")
user_schema = UserSchema()


class LoginBP(Resource):
    def post(self):
        try:
            data = request.get_json()

            email = data.get("email")
            password = data.get("password")
            if user := User.query.filter(User.email == email).first():
                if user.authenticate(password):
                    session["user_id"] = user.id
                    return make_response(user_schema.dump(user), 200)
            return make_response({"error": "Invalid credentials1"}, 401)
        except:
            return make_response({"error": "Invalid credentials2"}, 401)
