from sqlalchemy_serializer import SerializerMixin

from config import db, bcrypt


# needs: password stuffs, orphan logic adjust on comments
class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    profile_pic = db.Column(db.String)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    trips = db.relationship(
        "TripUser", back_populates="user", overlaps="admin_trips,admins", viewonly=True
    )
    admin_trips = db.relationship(
        "Trip", secondary="trip_users", back_populates="admins", overlaps="trips"
    )
    tasks = db.relationship("UserTask", back_populates="user")

    posts = db.relationship("Post", back_populates="user")
    comments = db.relationship("Comment", back_populates="user")
    post_likes = db.relationship("PostLike", back_populates="user")
    comment_likes = db.relationship("CommentLike", back_populates="user")
    travel_legs = db.relationship("TravelLeg", back_populates="user")

    def __repr__(self):
        return f"{self.__tablename__} id:{self.id}"


# needs: everything
class Trip(db.Model):
    __tablename__ = "trips"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String, nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime)
    location = db.Column(db.String, nullable=False)
    lodging = db.Column(db.String)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    users = db.relationship(
        "TripUser", back_populates="trip", overlaps="admin_trips", viewonly=True
    )
    admins = db.relationship(
        "User", secondary="trip_users", back_populates="admin_trips", overlaps="trips"
    )

    travel_legs = db.relationship("TravelLeg", back_populates="trip")
    events = db.relationship("Event", back_populates="trip")
    posts = db.relationship("Post", back_populates="trip")
    tasks = db.relationship("TripTask", back_populates="trip")
    # items = db.relationship("ItemTrip", back_populates="trip")

    def __repr__(self):
        return f"{self.__tablename__} id:{self.id}"


# needs: everything
class TripUser(db.Model):
    __tablename__ = "trip_users"

    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey("trips.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    is_admin = db.Column(db.Boolean, default=False)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    user = db.relationship(
        "User", back_populates="trips", overlaps="admin_trips,admins"
    )
    trip = db.relationship(
        "Trip", back_populates="users", overlaps="admin_trips,admins"
    )

    def __repr__(self):
        return f"{self.__tablename__} id:{self.id}"


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
