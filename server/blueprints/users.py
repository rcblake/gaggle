from flask import Blueprint, make_response, request
from flask_restful import Resource
from config import db
from models import User
from schema import UserSchema

user_bp = Blueprint("user", __name__, url_prefix="/users")

users_schema = UserSchema(many=True)
user_schema = UserSchema()


class UserResource(Resource):
    def get(self):
        users = User.query.all()
        serialized_users = users_schema.dump(users)
        return make_response(serialized_users, 200)

    def post(self):
        user_data = request.get_json()
        user = user_schema.load(user_data)
        db.session.add(user)
        db.session.commit()
        return make_response(user_schema.dump(user), 201)

    def get(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return make_response("User not found", 404)
        serialized_user = user_schema.dump(user)
        return make_response(serialized_user, 200)

    def patch(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return make_response("User not found", 404)
        user_data = request.get_json()
        user.name = user_data.get("name", user.name)
        #! Update other fields!
        db.session.commit()
        return make_response(user_schema.dump(user), 200)

    def delete(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return make_response("User not found", 404)
        db.session.delete(user)
        db.session.commit()
        return make_response("User deleted successfully", 204)
