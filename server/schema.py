from config import (
    db,
    bcrypt,
    Schema,
    fields,
    ValidationError,
    SQLAlchemySchema,
    SQLAlchemyAutoSchema,
    validate,
    validates,
)
from marshmallow_sqlalchemy.fields import Nested
from models import User


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_relationships = True

    name = fields.String(
        required=True,
        validate=validate.Length(max=20, error="Name must be less than 20 characters"),
    )
    email = fields.Email(required=True, error="invalid email address")

    admin_trips = Nested("TripSchema", many=True, exclude=("admins",))

    tasks = Nested("TaskSchema", many=True, exclude=("user"))
    posts = Nested("PostSchema", many=True, exclude=("user"))
    comments = Nested("CommentSchema", many=True, exclude=("user"))
    post_likes = Nested("PostLikeSchema", many=True, exclude=("user"))
    comment_likes = Nested("TripUserSchema", many=True, exclude=("user",))
    travel_legs = Nested("TripUserSchema", many=True, exclude=("user",))
