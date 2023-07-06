from sqlalchemy_serializer import SerializerMixin
from config import (
    db,
    bcrypt,
    Schema,
    fields,
    ValidationError,
    SQLAlchemySchema,
    SQLAlchemyAutoSchema,
    validate,
)
from marshmallow_sqlalchemy.fields import Nested
from datetime import date


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    _password_hash = db.Column(db.String, nullable=False)
    profile_pic = db.Column(db.String, nullable=True)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    trips = db.relationship("TripUser", back_populates="user")
    admin_trips = db.relationship(
        "Trip", secondary="trip_users", back_populates="admins"
    )
    tasks = db.relationship("UserTask", back_populates="user")

    posts = db.relationship("Post", back_populates="user")
    comments = db.relationship("Comment", back_populates="user")
    post_likes = db.relationship("PostLike", back_populates="user")
    comment_likes = db.relationship("CommentLike", back_populates="user")
    travel_legs = db.relationship("TravelLeg", back_populates="user")

    def __repr__(self):
        return f"{self.__tablename__} id:{self.id}"


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_relationships = True

    name = fields.String(
        required=True,
        validate=validate.length(max=20, error="Name must be less than 20 characters"),
    )
    email = fields.Email(required=True, error="invalid email address")

    admin_trips = Nested("TripSchema", many=True, exclude=("admins",))

    tasks = Nested("TaskSchema", many=True, exclude=("user"))
    posts = Nested("PostSchema", many=True, exclude=("user"))
    comments = Nested("CommentSchema", many=True, exclude=("user"))
    post_likes = Nested("PostLikeSchema", many=True, exclude=("user"))
    comment_likes = Nested("TripUserSchema", many=True, exclude=("user",))
    travel_legs = Nested("TripUserSchema", many=True, exclude=("user",))


class Trip(db.Model):
    __tablename__ = "trips"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String, nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime)
    location = db.Column(db.String, nullable=False)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    users = db.relationship("TripUser", back_populates="trip")
    admins = db.relationship(
        "User", secondary="trip_users", back_populates="admin_trips"
    )

    lodging = db.relationship("Lodging", back_populates="trip")
    travel_legs = db.relationship("TravelLeg", back_populates="trip")
    events = db.relationship("Event", back_populates="trip")
    posts = db.relationship("Post", back_populates="trip")
    tasks = db.relationship("TripTask", back_populates="trip")

    def __repr__(self):
        return f"{self.__tablename__} id:{self.id}"


class TripSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Trip
        include_relationships = True

    name = fields.String(
        required=True,
        validate=validate.length(max=20, error="Name must be less than 20 characters"),
    )
    start_date = fields.Date(
        required=True,
        validate=validate.range(
            min=date.today(), error="Start date must be in the future"
        ),
    )
    end_date = fields.Date(
        required=True,
        validate=validate.range(
            min=date.today(), error="End date must be in the future"
        ),
    )
    location = fields.String(
        validate=validate.Length(
            max=50, error="Location must be less than 50 characters"
        )
    )

    lodging = Nested("LodgingSchema", exclude=("trip",))
    users = Nested("TripUserSchema", many=True, exclude=("trip",))
    travel_legs = Nested("TravelLegSchema", many=True, exclude=("trip",))
    events = Nested("EventSchema", many=True, exclude=("trip",))
    posts = Nested("PostSchema", many=True, exclude=("trip",))
    tasks = Nested("TaskSchema", many=True, exclude=("trip",))
    admins = Nested("UserSchema", many=True, exclude=("admin_trips",))


class TripUser(db.Model):
    __tablename__ = "trip_users"

    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey("trips.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    is_admin = db.Column(db.Boolean, default=False)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    user = db.relationship("User", back_populates="trips")
    trip = db.relationship("Trip", back_populates="users")

    def __repr__(self):
        return f"{self.__tablename__} id:{self.id}"


class TripUserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = TripUser
        include_relationships = True

    user = Nested("UserSchema", exclude=("trips",))
    trip = Nested("TripSchema", exclude=("user",))


# needs: owner currently commented out, nullables, repr
class TripTask(db.Model):
    __tablename__ = "trip_tasks"

    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey("trips.id"))
    title = db.Column(db.String, nullable=False)
    note = db.Column(db.String, nullable=False)
    link = db.Column(db.String)
    cost = db.Column(db.Float)
    optional = db.Column(db.Boolean, default=True)
    everyone = db.Column(db.Boolean, default=False)
    # owner_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    child_tasks = db.relationship("UserTask", back_populates="parent_task")
    trip = db.relationship("Trip", back_populates="tasks")

    def __repr__(self):
        return f"{self.__tablename__} id:{self.id}"


# needs: everything
class UserTask(db.Model):
    __tablename__ = "user_tasks"

    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey("trips.id"))
    parent_task_id = db.Column(db.Integer, db.ForeignKey("trip_tasks.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    title = db.Column(db.String, nullable=False)
    note = db.Column(db.String, nullable=False)
    link = db.Column(db.String)
    cost = db.Column(db.Float)
    optional = db.Column(db.Boolean, default=True)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    parent_task = db.relationship("TripTask", back_populates="child_tasks")
    user = db.relationship("User", back_populates="tasks")

    def __repr__(self):
        return f"{self.__tablename__} id:{self.id}"


# needs: everything
class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey("trips.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    content = db.Column(db.String, nullable=False)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    trip = db.relationship("Trip", back_populates="posts")
    user = db.relationship("User", back_populates="posts")
    comments = db.relationship("Comment", back_populates="post")
    post_likes = db.relationship("PostLike", back_populates="post")

    def __repr__(self):
        return f"{self.__tablename__} id:{self.id}"


# needs: everything
class Comment(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    content = db.Column(db.String, nullable=False)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    post = db.relationship("Post", back_populates="comments")
    user = db.relationship("User", back_populates="comments")
    comment_likes = db.relationship("CommentLike", back_populates="comment")

    def __repr__(self):
        return f"{self.__tablename__} id:{self.id}"


# needs: everything
class PostLike(db.Model):
    __tablename__ = "post_likes"

    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    post = db.relationship("Post", back_populates="post_likes")
    user = db.relationship("User", back_populates="post_likes")

    def __repr__(self):
        return f"{self.__tablename__} id:{self.id}"


# needs: everything
class CommentLike(db.Model):
    __tablename__ = "comment_likes"

    id = db.Column(db.Integer, primary_key=True)
    comment_id = db.Column(db.Integer, db.ForeignKey("comments.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    comment = db.relationship("Comment", back_populates="comment_likes")
    user = db.relationship("User", back_populates="comment_likes")

    def __repr__(self):
        return f"{self.__tablename__} id:{self.id}"


# needs: everything
class Event(db.Model):
    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey("trips.id"))
    title = db.Column(db.String, nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime)
    link = db.Column(db.String)
    ticketed = db.Column(db.Boolean, default=False)
    price = db.Column(db.Float)
    note = db.Column(db.String)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    trip = db.relationship("Trip", back_populates="events")

    def __repr__(self):
        return f"{self.__tablename__} id:{self.id}"


# needs: everything
class TravelLeg(db.Model):
    __tablename__ = "travel_legs"

    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey("trips.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    travel_type = db.Column(db.String)
    departure_time = db.Column(db.DateTime, nullable=False)
    arrival_time = db.Column(db.DateTime, nullable=False)
    flight_number = db.Column(db.String)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    trip = db.relationship("Trip", back_populates="travel_legs")
    user = db.relationship("User", back_populates="travel_legs")

    def __repr__(self):
        return f"{self.__tablename__} id:{self.id}"


class Lodging(db.Model):
    __tablename__ = "lodgings"

    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey("trips.id"))
    link = db.Column(db.String)
    note = db.Column(db.String)

    trip = db.relationship("Trip", back_populates="lodging")
