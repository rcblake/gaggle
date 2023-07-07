from faker import Faker
from datetime import timedelta

from config import db, app
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

fake = Faker()


def create_fake_user():
    name = fake.name()
    email = fake.email()
    # password = fake.password()
    profile_pic = fake.image_url()

    user = User(name=name, email=email, profile_pic=profile_pic)
    db.session.add(user)
    db.session.commit()

    return user


def create_fake_trip():
    name = fake.word()
    start_date = fake.date_time_this_year()
    end_date = start_date + timedelta(days=7)
    location = fake.city()
    lodging = fake.word()

    trip = Trip(
        name=name,
        start_date=start_date,
        end_date=end_date,
        location=location,
    )
    db.session.add(trip)
    db.session.commit()

    return trip


def create_fake_trip_user(trip, user):
    is_admin = fake.boolean()

    trip_user = TripUser(trip=trip, user=user, is_admin=is_admin)
    db.session.add(trip_user)
    db.session.commit()

    return trip_user


def create_fake_trip_task(trip):
    title = fake.sentence()
    note = fake.paragraph()
    link = fake.url()
    cost = fake.pyfloat()
    optional = fake.boolean()
    everyone = fake.boolean()

    trip_task = TripTask(
        trip=trip,
        title=title,
        note=note,
        link=link,
        cost=cost,
        optional=optional,
        everyone=everyone,
    )
    db.session.add(trip_task)
    db.session.commit()

    return trip_task


def create_fake_user_task(trip_task):
    title = fake.sentence()
    note = fake.paragraph()
    link = fake.url()
    cost = fake.pyfloat()
    optional = fake.boolean()

    user_task = UserTask(
        parent_task=trip_task,
        title=title,
        note=note,
        link=link,
        cost=cost,
        optional=optional,
    )
    db.session.add(user_task)
    db.session.commit()

    return user_task


def create_fake_post(trip, user):
    content = fake.paragraph()

    post = Post(trip=trip, user=user, content=content)
    db.session.add(post)
    db.session.commit()

    return post


def create_fake_comment(post, user):
    content = fake.paragraph()

    comment = Comment(post=post, user=user, content=content)
    db.session.add(comment)
    db.session.commit()

    return comment


def create_fake_post_like(post, user):
    post_like = PostLike(post=post, user=user)
    db.session.add(post_like)
    db.session.commit()

    return post_like


def create_fake_comment_like(comment, user):
    comment_like = CommentLike(comment=comment, user=user)
    db.session.add(comment_like)
    db.session.commit()

    return comment_like


def create_fake_event(trip):
    title = fake.sentence()
    start_time = fake.date_time_this_year()
    end_time = start_time + timedelta(hours=2)
    link = fake.url()
    ticketed = fake.boolean()
    price = fake.pyfloat()
    note = fake.paragraph()

    event = Event(
        trip=trip,
        title=title,
        start_time=start_time,
        end_time=end_time,
        link=link,
        ticketed=ticketed,
        price=price,
        note=note,
    )
    db.session.add(event)
    db.session.commit()

    return event


def create_fake_travel_leg(trip, user):
    travel_type = fake.word()
    departure_time = fake.date_time_this_year()
    arrival_time = departure_time + timedelta(hours=3)
    flight_number = fake.word()

    travel_leg = TravelLeg(
        trip=trip,
        user=user,
        travel_type=travel_type,
        departure_time=departure_time,
        arrival_time=arrival_time,
        flight_number=flight_number,
    )
    db.session.add(travel_leg)
    db.session.commit()

    return travel_leg


def create_fake_trip_lodging(trip):
    link = fake.url()
    note = fake.paragraph()

    lodging = Lodging(trip=trip, link=link, note=note)
    db.session.add(lodging)
    db.session.commit()

    return lodging


# Usage example:
if __name__ == "__main__":
    with app.app_context():
        User.query.delete()
        Trip.query.delete()
        TripUser.query.delete()
        TripTask.query.delete()
        UserTask.query.delete()
        Post.query.delete()
        Comment.query.delete()
        PostLike.query.delete()
        CommentLike.query.delete()
        Event.query.delete()
        TravelLeg.query.delete()
        Lodging.query.delete()

        # Create some fake users
        users = [create_fake_user() for _ in range(5)]

        # Create a fake trip
        trip = create_fake_trip()

        # Add users to the trip as trip users
        for user in users:
            create_fake_trip_user(trip, user)

        # Create fake trip tasks
        for _ in range(3):
            trip_task = create_fake_trip_task(trip)

            # Create fake user tasks for each trip task
            for _ in range(20):
                create_fake_user_task(trip_task)

        # Create fake posts
        for user in users:
            create_fake_post(trip, user)

        # Create fake comments
        posts = Post.query.filter_by(trip_id=trip.id).all()
        for post in posts:
            for _ in range(20):
                create_fake_comment(post, users[fake.random_int(0, len(users) - 1)])

        # Create fake post likes
        posts = Post.query.filter_by(trip_id=trip.id).all()
        for post in posts:
            for _ in range(fake.random_int(0, len(users) // 2)):
                create_fake_post_like(post, users[fake.random_int(0, len(users) - 1)])

        # Create fake comment likes
        comments = Comment.query.join(Post).filter(Post.trip_id == trip.id).all()
        for comment in comments:
            for _ in range(fake.random_int(0, len(users) // 2)):
                create_fake_comment_like(
                    comment, users[fake.random_int(0, len(users) - 1)]
                )

        # Create fake events
        for _ in range(10):
            create_fake_event(trip)

        # Create fake travel legs
        for user in users:
            create_fake_travel_leg(trip, user)
