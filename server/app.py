#!/usr/bin/env python3
import ipdb
from flask import make_response

# Standard library imports

# Remote library imports
from flask_restful import Resource

# Local imports
from config import app, api

from blueprints.user import User, user_bp
from blueprints.trip import Trip, trip_bp
from blueprints.trip_user import TripUser, trip_user_bp
from blueprints.trip_task import TripTask, trip_task_bp
from blueprints.user_task import UserTask, user_task_bp
from blueprints.post import Post, post_bp
from blueprints.comment import Comment, comment_bp
from blueprints.post_like import PostLike, post_like_bp
from blueprints.comment_like import CommentLike, comment_like_bp
from blueprints.event import Event, event_bp
from blueprints.travel_leg import TravelLeg, travel_leg_bp
from blueprints.lodging import Lodging, lodging_bp

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

api.add_resource(User, "/users", "/users/<int:user_id>")
api.add_resource(Trip, "/trips", "/trips/<int:trip_id>")
api.add_resource(TripUser, "/trip_users", "/trip_users/<int:trip_user_id>")
api.add_resource(TripTask, "/trip_tasks", "/trip_tasks/<int:trip_task_id>")
api.add_resource(UserTask, "/user_tasks", "/user_tasks/<int:user_task_id>")
api.add_resource(Post, "/posts", "/posts/<int:post_id>")
api.add_resource(Comment, "/comments", "/comments/<int:comment_id>")
api.add_resource(PostLike, "/post_likes", "/post_likes/<int:post_like_id>")
api.add_resource(CommentLike, "/comment_likes", "/comment_likes/<int:comment_like_id>")
api.add_resource(Event, "/events", "/events/<int:event_id>")
api.add_resource(TravelLeg, "/travel_legs", "/travel_legs/<int:travel_leg_id>")
api.add_resource(Lodging, "/lodgings", "/lodgings/<int:lodging_id>")


# Views go here!

if __name__ == "__main__":
    app.run(port=5555, debug=True)
