#!/usr/bin/env python3

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

from blueprints.users import Users
from blueprints.users_by_id import UsersById

api.add_resource(Users, "/users")
api.add_resource(UsersById, "/user/<int:id>")


# Views go here!

if __name__ == "__main__":
    app.run(port=5555, debug=True)
