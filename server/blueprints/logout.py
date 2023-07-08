from blueprints import request, session, Resource, Blueprint, make_response, g, abort 
from blueprints.user_by_id import user_schema
from models import db
from models.user import User

logout_bp = Blueprint("logout", __name__, url_prefix="/logout")

class Logout(Resource):
    def delete(self): 
        if session.get('user_id'):
            session['user_id'] = None
            return make_response({}, 204)
        return make_response({'error': 'Unauthorized'}, 401)