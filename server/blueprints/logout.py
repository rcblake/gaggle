from blueprints import session, Resource, Blueprint, make_response, g, abort
from models import db

logout_bp = Blueprint("logout", __name__, url_prefix="/api/v1/logout")


class LogoutBP(Resource):
    def delete(self):
        if session.get("user_id"):
            session["user_id"] = None
            return make_response({}, 204)
        return make_response({"error": "Unauthorized"}, 401)
