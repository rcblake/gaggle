from blueprints import request, session, Resource, Blueprint, make_response, g, abort 
from blueprints.user_by_id import user_schema
from models import db
from models.user import User

login_bp = Blueprint("login", __name__, url_prefix="/login")

class Login(Resource):
    def post(self): 
        try:
            data = request.get_json()
            
            username = data.get('username')
            password = data.get('password')
            if user := User.query.filter(User.username == username).first():
                if user.authenticate(password):
                    session['user_id'] = user.id
                    return make_response(user_schema.dump(user), 200)
            return make_response({'error': 'Invalid credentials'}, 401)
        except: 
            return make_response({'error': 'Invalid credentials'}, 401) 