from sqlalchemy_serializer import SerializerMixin

from config import db, bcrypt


# needs: password stuffs, orphan logic adjust on comments
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    profile_pic = db.Column(db.String)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    trips = db.relationship("TripUser", back_populates="user")
    admin_trips = db.relationship(
        "Trip", secondary="trip_user", back_populates="admins"
    )
    tasks = db.relationship("TaskUser", back_populates="user")

    posts = db.relationship("Post", back_populates="user")
    comments = db.relationship("Comment", back_populates="user")
    post_likes = db.relationship("PostLike", back_populates="user")
    comment_likes = db.relationship("CommentLike", back_populates="user")

    def __repr__(self):
        return f"{self.__tablename__} id:{self.id}"


# needs: everything
class Trip(db.Model):
    __tablename__ = "trips"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    location = db.Column(db.String)
    lodging = db.Column(db.String)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    users = db.relationship("TripUser", back_populates="trip")
    admins = db.relationship(
        "User", secondary="trip_user", back_populates="admin_trips"
    )

    travels_legs = db.relationship("TravelLeg", back_populates="trip")
    events = db.relationship("Events", back_populates="trip")
    posts = db.relationship("Post", back_populates="trip")
    tasks = db.relationship("TaskTrip", back_populates="trip")
    items = db.relationship("ItemTrip", back_populates="trip")

    def __repr__(self):
        return f"{self.__tablename__} id:{self.id}"


# needs: everything
class TripUser(db.Model):
    __tablename__ = "trips_users"

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


# needs: owner currently commented out, nullables, repr
class TripTask(db.Model):
    __tablename__ = "trip_tasks"

    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey("trips.id"))
    name = db.Column(db.String)
    note = db.Column(db.String)
    link = db.Column(db.String)
    cost = db.Column(db.Float)
    optional = db.Column(db.Boolean, default=True)
    everyone = db.Column(db.Boolean, default=False)
    # owner_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    child_tasks = db.relationship(
        "UserTask", back_populates="parent_task", nullable=True
    )

    def __repr__(self):
        return f"{self.__tablename__} id:{self.id}"


# needs: everything
class UserTask(db.Model):
    __tablename__ = "user_tasks"

    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey("trips.id"))
    parent_task_id = db.Column(db.Integer, db.ForeignKey("tasks"), nullable=True)
    name = db.Column(db.String)
    note = db.Column(db.String)
    link = db.Column(db.String)
    cost = db.Column(db.Float)
    optional = db.Column(db.Boolean, default=True)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    parent_task = db.relationship(
        "TripTask", back_populates="child_tasks", nullable=True
    )

    def __repr__(self):
        return f"{self.__tablename__} id:{self.id}"


# needs: everything
class Post(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey("trips.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    content = db.Column(db.String)

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
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    content = db.Column(db.String)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    post = db.relationship("Post", back_populates="comments")
    user = db.relationship("User", back_populates="comments")
    comment_likes = db.relationship("PostLike", back_populates="comment")

    def __repr__(self):
        return f"{self.__tablename__} id:{self.id}"


# needs: everything
class PostLike(db.Model):
    __tablename__ = "users"

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
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    comment_id = db.Column(db.Integer, db.ForeignKey("comments.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    comment = db.relationship("Post", back_populates="comment_likes")
    user = db.relationship("User", back_populates="comment_likes")

    def __repr__(self):
        return f"{self.__tablename__} id:{self.id}"


# needs: everything
class Event(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey("trips.id"))
    name = db.Column(db.String)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    link = db.Column(db.String)
    ticketed = db.Column(db.Boolean, default=False)
    price = db.Column(db.Float)
    note = db.Column(db.String)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f"{self.__tablename__} id:{self.id}"


# needs: everything
class TravelLeg(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f"{self.__tablename__} id:{self.id}"

    # # needs: everything
    # class ItemTrip(db.Model):
    #     __tablename__ = "users"

    #     id = db.Column(db.Integer, primary_key=True)

    #     created_at = db.Column(db.DateTime, server_default=db.func.now())
    #     updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    #     def __repr__(self):
    #         return f"{self.__tablename__} id:{self.id}"

    # # needs: everything
    # class ItemUser(db.Model):
    #     __tablename__ = "users"

    #     id = db.Column(db.Integer, primary_key=True)

    #     created_at = db.Column(db.DateTime, server_default=db.func.now())
    #     updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    #     def __repr__(self):
    #         return f"{self.__tablename__} id:{self.id}"

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f"{self.__tablename__} id:{self.id}"
