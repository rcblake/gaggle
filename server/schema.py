from config import (
    db,
    bcrypt,
    Schema,
    fields,
    ValidationError,
    SQLAlchemyAutoSchema,
    validate,
    validates_schema,
    validates,
)
from marshmallow_sqlalchemy.fields import Nested
from models import (
    User,
    Trip,
    TripUser,
    Task,
    Event,
    TravelLeg,
    Lodging,
)

from datetime import date
import ipdb


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_relationships = True
        load_instance = True
        fields = ("id", "name", "email", "trips", "travel_legs")

    name = fields.String(
        required=True,
        validate=validate.Length(max=20, error="Name must be less than 20 characters"),
    )
    email = fields.Email(required=True, error="invalid email address")

    trips = Nested(
        "TripUserSchema",
        many=True,
        only=("trip.id", "trip.name", "trip.start_date", "trip.end_date"),
    )

    travel_legs = Nested("TravelLegSchema", many=True)

    @validates("email")
    def validates_email(self, email):
        if user := User.query.filter(User.email == email).first():
            if not user.id:
                raise ValidationError("An account already exists with that email.")


class TripSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Trip
        include_relationships = True
        load_instance = True
        fields = (
            "id",
            "name",
            "location",
            "start_date",
            "end_date",
            "lodging",
            "users",
            "travel_legs",
            "tasks",
        )

    name = fields.String(
        validate=validate.Length(max=20, error="Name must be less than 20 characters"),
    )
    start_date = fields.Date(
        required=True,
        validate=validate.Range(
            min=date.today(), error="Start date must be in the future"
        ),
    )
    end_date = fields.Date(
        required=True,
    )

    lodging = Nested("LodgingSchema", many=True)
    users = Nested(
        "TripUserSchema",
        many=True,
        only=(
            "user.id",
            "user.name",
            "user.email",
        ),
    )
    travel_legs = Nested("TravelLegSchema", many=True)
    tasks = Nested("TaskSchema", many=True)
    events = Nested("EventSchema", many=True)

    @validates_schema
    def validate_end_date(self, data, **kwargs):
        start = data.get("start_date")
        end = data.get("end_date")
        if end and start and end < start:
            raise ValidationError("End date must be after start date")


class TripUserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = TripUser
        include_relationships = True
        load_instance = True

    user_id = fields.Integer(required=True)
    trip_id = fields.Integer(required=True)
    is_admin = fields.Boolean(missing=False)

    user = Nested("UserSchema", exclude=("trips",))
    trip = Nested("TripSchema", exclude=("users",))


class TaskSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Task
        include_relationships = True
        load_instance = True

    trip = Nested("TripSchema", only=("id",))


class EventSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Event
        include_relationships = True
        load_instance = True

    trip = Nested("TripSchema", exclude=("events",))


class TravelLegSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = TravelLeg
        include_relationships = True
        load_instance = True

    trip = Nested("TripSchema", only=("id",))
    user = Nested("UserSchema", only=("id", "name"))


class LodgingSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Lodging
        include_relationships = True
        load_instance = True

    trip = Nested("TripSchema", only=("lodging",))
