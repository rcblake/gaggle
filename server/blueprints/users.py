from blueprints import Resource, Blueprint, make_response, g, abort
from config import db
from models import User
from schema import UserSchema

users_schema = UserSchema(many=True)
user_bp = Blueprint("users", __name__, url_prefix="/users")


class Users(Resource):
    def get(self):
        users = users_schema.dump(User.query.all())
        return make_response(users, 200)
