from faker import Faker
from datetime import timedelta

from config import db, app
from models import (
    User,
    Trip,
    TripUser,
    Task,
    Event,
    TravelLeg,
    Lodging,
)

fake = Faker()


def create_fake_user():
    name = fake.name()
    email = fake.email()
    _password_hash = fake.password()

    user = User(name=name, email=email, _password_hash=_password_hash)
    db.session.add(user)
    db.session.commit()

    return user


def create_fake_trip():
    name = fake.word()
    start_date = fake.date_time_this_year()
    end_date = start_date + timedelta(days=7)
    location = fake.city()

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
    trip_user = TripUser(trip=trip, user=user)
    db.session.add(trip_user)
    db.session.commit()

    return trip_user


def create_fake_task(trip):
    title = fake.sentence()
    note = fake.paragraph()
    link = fake.url()
    cost = fake.pyfloat()
    optional = fake.boolean()
    everyone = fake.boolean()

    task = Task(
        trip=trip,
        title=title,
        note=note,
        link=link,
        cost=cost,
        optional=optional,
        everyone=everyone,
    )
    db.session.add(task)
    db.session.commit()

    return task


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
        Task.query.delete()
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
            task = create_fake_task(trip)

        # Create fake events
        for _ in range(3):
            create_fake_event(trip)

        # Create fake travel legs
        for user in users:
            create_fake_travel_leg(trip, user)

        for _ in range(1):
            create_fake_trip_lodging(trip)
