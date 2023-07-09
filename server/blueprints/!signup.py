from blueprints import request, session, Resource, Blueprint, make_response, g, abort
from blueprints.user import user_schema
from models import db
from models import User


signup_bp = Blueprint("signup", __name__, url_prefix="/signup")


class Signup(Resource):
    def post(self):
        try:
            data = request.get_json()

            email = data.get("email")
            password = data.get("password")

            if User.query.filter(User.email == email).first():
                return make_response({"error": "Username must be unique"}, 400)

            new_user = User(email=email)
            new_user.password_hash = password

            db.session.add(new_user)
            db.session.commit()

            session["user_id"] = new_user.id

            return make_response(user_schema.dump(new_user), 201)
        except Exception as e:
            return make_response({"error": [str(e)]}, 422)
