from config import (
    db,
    bcrypt,
)
from sqlalchemy.ext.hybrid import hybrid_property


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    _password_hash = db.Column(db.String)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    travel_legs = db.relationship(
        "TravelLeg", back_populates="user", cascade="all, delete-orphan"
    )

    trips = db.relationship(
        "TripUser", back_populates="user", cascade="all, delete-orphan"
    )

    @hybrid_property
    def password_hash(self):
        raise AttributeError("Password hashes may not be viewed")

    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode("utf-8"))
        self._password_hash = password_hash.decode("utf-8")

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode("utf-8"))


class Trip(db.Model):
    __tablename__ = "trips"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    location = db.Column(db.String, nullable=False)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    lodging = db.relationship(
        "Lodging", back_populates="trip", cascade="all, delete-orphan"
    )
    travel_legs = db.relationship(
        "TravelLeg", back_populates="trip", cascade="all, delete-orphan"
    )
    events = db.relationship(
        "Event", back_populates="trip", cascade="all, delete-orphan"
    )
    tasks = db.relationship("Task", back_populates="trip", cascade="all, delete-orphan")

    users = db.relationship(
        "TripUser", back_populates="trip", cascade="all, delete-orphan"
    )


class TripUser(db.Model):
    __tablename__ = "trip_users"

    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey("trips.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    user = db.relationship("User", back_populates="trips")
    trip = db.relationship("Trip", back_populates="users")


# needs: owner currently commented out, nullables, repr
class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey("trips.id"))
    title = db.Column(db.String, nullable=False)
    note = db.Column(db.String, nullable=False)
    link = db.Column(db.String, nullable=True)
    cost = db.Column(db.Float, nullable=True)
    optional = db.Column(db.Boolean, default=False)
    everyone = db.Column(db.Boolean, default=True)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    trip = db.relationship("Trip", back_populates="tasks")


# needs: everything


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


class Lodging(db.Model):
    __tablename__ = "lodgings"

    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey("trips.id"))
    link = db.Column(db.String)
    note = db.Column(db.String)

    trip = db.relationship("Trip", back_populates="lodging")
