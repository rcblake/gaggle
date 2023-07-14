from config import (
    db,
    bcrypt,
    Schema,
    fields,
    ValidationError,
    SQLAlchemyAutoSchema,
    validate,
    validates,
)
from marshmallow_sqlalchemy.fields import Nested
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

from datetime import date


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_relationships = True
        load_instance = True

    name = fields.String(
        validate=validate.Length(max=20, error="Name must be less than 20 characters"),
    )
    email = fields.Email(required=True, error="invalid email address")

    trips = Nested("TripUserSchema")
    admin_trips = Nested("TripSchema", exclude=("admins",))

    tasks = Nested("UserTaskSchema")
    posts = Nested("PostSchema")
    comments = Nested("CommentSchema")
    post_likes = Nested("PostLikeSchema")
    comment_likes = Nested("CommentLikeSchema")
    travel_legs = Nested("TravelLegSchema")


class TripSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Trip
        include_relationships = True

    tripName = fields.String(
        required=True,
        validate=validate.Length(max=20, error="Name must be less than 20 characters"),
    )
    startDate = fields.Date(
        required=True,
        validate=validate.Range(
            min=date.today(), error="Start date must be in the future"
        ),
    )

    lodging = Nested("LodgingSchema", many=True, exclude=("trip",))
    users = Nested(
        "TripUserSchema",
        many=True,
        only=(
            "user.id",
            "user.name",
            "user.email",
        ),
    )
    travel_legs = Nested("TravelLegSchema", many=True, exclude=("trip",))
    events = Nested("EventSchema", many=True, exclude=("trip",))
    posts = Nested("PostSchema", many=True, exclude=("trip",))
    tasks = Nested("TripTaskSchema", many=True, exclude=("trip",))
    admins = Nested(
        "UserSchema",
        many=True,
        only=(
            "id",
            "name",
            "email",
        ),
    )

    @validates("end_date")
    def validate_end_date(self, value, **kwargs):
        if value < self.start_date:
            raise ValidationError("End date must be after Start date")


class TripUserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = TripUser
        include_relationships = True

    user = Nested("UserSchema", exclude=("trips",))
    trip = Nested("TripSchema", exclude=("users",))


class TripTaskSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = TripTask
        include_relationships = True

    trip = Nested("TripSchema", exclude=("tasks",))


class UserTaskSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = UserTask
        include_relationships = True


class UserTaskSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = UserTask
        include_relationships = True

    user = Nested("UserSchema", exclude=("tasks",))


class PostSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Post
        include_relationships = True

    trip = Nested("TripSchema", exclude=("posts",))
    user = Nested("UserSchema", only=("id", "name"))
    comments = Nested("CommentSchema", exclude=("post",))
    post_likes = Nested("PostLikeSchema", exclude=("post",))


class CommentSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Comment
        include_relationships = True

    post = Nested("PostSchema", exclude=("comments",))
    user = Nested("UserSchema", only=("id", "name"))
    comment_likes = Nested("CommentLikeSchema", exclude=("comment",))


class PostLikeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = PostLike
        include_relationships = True

    post = Nested("PostSchema", exclude=("post_likes",))
    user = Nested("UserSchema", only=("id", "name"))


class CommentLikeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = CommentLike
        include_relationships = True

    comment = Nested("CommentSchema", exclude=("comment_likes",))
    user = Nested("UserSchema", only=("id", "name"))


class EventSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Event
        include_relationships = True

    trip = Nested("TripSchema", exclude=("events",))


class TravelLegSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = TravelLeg
        include_relationships = True

    trip = Nested("TripSchema", exclude=("travel_legs",))
    user = Nested("UserSchema", only=("id", "name"))


class LodgingSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Lodging
        include_relationships = True

    trip = Nested("TripSchema", only=("lodging",))
