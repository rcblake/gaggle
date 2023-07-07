from flask import Blueprint, make_response, g, abort, request, session
from flask_restful import Resource
from config import db
from models import User
from schema import UserSchema

user_schema = UserSchema()

user_by_id_bp = Blueprint("user_by_id", __name__, url_prefix="/users/<int:id>")


class UsersById(Resource):
    def get(self, id):
        user = user_schema.dump(db.session.get(User, id))
        if user:
            return make_response(user, 200)
        return make_response({"error": "User not found"}, 404)

    # def patch(self, id):
    #     if user := db.session.get(User, id):
    #         try:
    #             if user.id == session["user_id"]:
    #                 data = request.get_json()
    #                 data["id"] = user.id
    #                 user_schema.validate(data)

    #                 updated_user = user_schema.load(data, instance=user, partial=True)
    #                 db.session.commit()

    #                 return make_response(user_schema.dump(updated_user), 200)
    #             return make_response({"error": "Unauthorized"}, 401)

    #         except Exception as e:
    #             db.session.rollback()
    #             return make_response({"errors": [str(e)]}, 400)
    #     return make_response({"error": "User not found"}, 404)

    # def delete(self, id):
    #     if user := db.session.get(User, id):
    #         try:
    #             current_user = db.session.get(User, session["user_id"])
    #             if user == current_user:
    #                 db.session.delete(user)
    #                 db.session.commit()

    #                 return make_response("", 204)
    #             return make_response({"error": "Unauthorized"}, 401)
    #         except Exception as e:
    #             db.session.rollback()
    #             return make_response({"errors": [str(e)]}, 400)
    #     return make_response({"error": "User not found"}, 404)
