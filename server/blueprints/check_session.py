from blueprints import request, session, Resource, Blueprint, make_response, g, abort
from blueprints.users_by_id import user_schema
from config import db
from models import User

check_session_bp = Blueprint("check_session", __name__, url_prefix="/check_session")


class CheckSession(Resource):
    def get(self):
        if id := session.get("user_id"):
            if user := db.session.get(User, id):
                return make_response(user_schema.dump(user), 200)
        # return make_response({'error': 'Unauthorized'}, 401)
