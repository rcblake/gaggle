#!/usr/bin/env python3
import ipdb
from flask import make_response

# Standard library imports

# Remote library imports
from flask import request
from flask_restful import Resource

# Local imports
from config import app, db, api
from models import (
    User,
    Trip,
    TripUser,
    TripTask,
    UserTask,
    Post,
    Comment,
    PostLike,
    CommentLike,
    Event,
    TravelLeg,
    Lodging,
)
from schema import (
    UserSchema,
    TripSchema,
    TripUserSchema,
    TripTaskSchema,
    UserTaskSchema,
    PostSchema,
    CommentSchema,
    PostLikeSchema,
    CommentLikeSchema,
    EventSchema,
    TravelLegSchema,
    LodgingSchema,
)

from blueprints.users import UserResource, user_bp
from blueprints.trip import TripResource, trip_bp
from blueprints.trip_user import TripUserResource, trip_user_bp
from blueprints.trip_task import TripTaskResource, trip_task_bp
from blueprints.user_task import UserTaskResource, user_task_bp
from blueprints.post import PostResource, post_bp
from blueprints.comment import CommentResource, comment_bp
from blueprints.post_like import PostLikeResource, post_like_bp
from blueprints.comment_like import CommentLikeResource, comment_like_bp
from blueprints.event import EventResource, event_bp
from blueprints.travel_leg import TravelLegResource, travel_leg_bp
from blueprints.lodging import LodgingResource, lodging_bp

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

api.add_resource(UserResource, "/users", "/users/<int:user_id>")
api.add_resource(TripResource, "/trips", "/trips/<int:trip_id>")
api.add_resource(TripUserResource, "/trip_users", "/trip_users/<int:trip_user_id>")
api.add_resource(TripTaskResource, "/trip_tasks", "/trip_tasks/<int:trip_task_id>")
api.add_resource(UserTaskResource, "/user_tasks", "/user_tasks/<int:user_task_id>")
api.add_resource(PostResource, "/posts", "/posts/<int:post_id>")
api.add_resource(CommentResource, "/comments", "/comments/<int:comment_id>")
api.add_resource(PostLikeResource, "/post_likes", "/post_likes/<int:post_like_id>")
api.add_resource(
    CommentLikeResource, "/comment_likes", "/comment_likes/<int:comment_like_id>"
)
api.add_resource(EventResource, "/events", "/events/<int:event_id>")
api.add_resource(TravelLegResource, "/travel_legs", "/travel_legs/<int:travel_leg_id>")
api.add_resource(LodgingResource, "/lodgings", "/lodgings/<int:lodging_id>")


# from schema import UserSchema

# user_schema = UserSchema()


# class UsersById(Resource):
#     def get(self, id):
#         user = user_schema.dump(db.session.get(User, id))
#         if user:
#             return make_response(user, 200)
#         return make_response({"error": "User not found"}, 404)


# api.add_resource(UsersById, "/users/<int:id>")


# class Posts(Resource):
#     pass


# api.add_resource(Posts, "/posts")


# #
# class Comments(Resource):
#     pass


# api.add_resource(Posts, "/comments")


# #
# class PostsById(Resource):
#     pass


# api.add_resource(PostsById, "/posts/<int:id>")


# #
# class CommentsById(Resource):
#     pass


# api.add_resource(CommentsById, "/comments/<int:id>")


# #
# class Events(Resource):
#     pass


# api.add_resource(Events, "/events")


# #
# class TripTasks(Resource):
#     pass


# api.add_resource(TripTasks, "/trip_tasks")


# #
# class Trips(Resource):
#     pass


# api.add_resource(Trips, "/Trips")


# #
# class UserTasks(Resource):
#     pass


# api.add_resource(UserTasks, "/user_tasks")


# #
# class PostLikes(Resource):
#     pass


# api.add_resource(PostLikes, "/post_likes")


# #
# class CommentLikes(Resource):
#     pass


# api.add_resource(CommentLikes, "/comment_likes")


# #
# class TravelLegs(Resource):
#     pass


# api.add_resource(TravelLegs, "/travel_legs")


# #
# class Lodgings(Resource):
#     pass


# api.add_resource(Lodgings, "/lodgings")


# #
# class CommentLikes(Resource):
#     pass


# api.add_resource(CommentLikes, "/comment_likes")


# #
# class CommentLikes(Resource):
#     pass


# api.add_resource(CommentLikes, "/comment_likes")


# #
# class CommentLikes(Resource):
#     pass


# api.add_resource(CommentLikes, "/comment_likes")
# #


# Views go here!

if __name__ == "__main__":
    app.run(port=5555, debug=True)
