#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask_restful import Resource

# Local imports
from config import app, api, render_template

from blueprints.user import UserBP, user_bp
from blueprints.trip import TripBP, trip_bp
from blueprints.trip_user import TripUserBP, trip_user_bp
from blueprints.trip_task import TripTaskBP, trip_task_bp
from blueprints.user_task import UserTaskBP, user_task_bp
from blueprints.post import PostBP, post_bp
from blueprints.comment import CommentBP, comment_bp
from blueprints.post_like import PostLikeBP, post_like_bp
from blueprints.comment_like import CommentLikeBP, comment_like_bp
from blueprints.event import EventBP, event_bp
from blueprints.travel_leg import TravelLegBP, travel_leg_bp
from blueprints.lodging import LodgingBP, lodging_bp
from blueprints.check_session import CheckSessionBP, check_session_bp
from blueprints.signup import SignupBP, signup_bp
from blueprints.login import LoginBP, login_bp
from blueprints.logout import LogoutBP, logout_bp

app.register_blueprint(user_bp)
app.register_blueprint(trip_bp)
app.register_blueprint(trip_user_bp)
app.register_blueprint(trip_task_bp)
app.register_blueprint(user_task_bp)
app.register_blueprint(post_bp)
app.register_blueprint(comment_bp)
app.register_blueprint(post_like_bp)
app.register_blueprint(comment_like_bp)
app.register_blueprint(event_bp)
app.register_blueprint(travel_leg_bp)
app.register_blueprint(lodging_bp)
app.register_blueprint(check_session_bp)
app.register_blueprint(signup_bp)
app.register_blueprint(login_bp)
app.register_blueprint(logout_bp)

api.add_resource(UserBP, "/users", "/users/<int:user_id>")
api.add_resource(TripBP, "/trips", "/trips/<int:trip_id>")
api.add_resource(TripUserBP, "/trip_users", "/trip_users/<int:trip_user_id>")
api.add_resource(TripTaskBP, "/trip_tasks", "/trip_tasks/<int:trip_task_id>")
api.add_resource(UserTaskBP, "/user_tasks", "/user_tasks/<int:user_task_id>")
api.add_resource(PostBP, "/posts", "/posts/<int:post_id>")
api.add_resource(CommentBP, "/comments", "/comments/<int:comment_id>")
api.add_resource(PostLikeBP, "/post_likes", "/post_likes/<int:post_like_id>")
api.add_resource(
    CommentLikeBP, "/comment_likes", "/comment_likes/<int:comment_like_id>"
)
api.add_resource(EventBP, "/events", "/events/<int:event_id>")
api.add_resource(TravelLegBP, "/travel_legs", "/travel_legs/<int:travel_leg_id>")
api.add_resource(LodgingBP, "/lodgings", "/lodgings/<int:lodging_id>")
api.add_resource(CheckSessionBP, "/check_session")
api.add_resource(SignupBP, "/signup")
api.add_resource(LoginBP, "/login")
api.add_resource(LogoutBP, "/logout")


# Views go here!
def register_routes():
    @app.route("/")
    @app.route("/login")
    @app.route("/trips/<int:id>")
    def index(id=0):
        return render_template("index.html")


if __name__ == "__main__":
    app.run(port=5555, debug=True)
