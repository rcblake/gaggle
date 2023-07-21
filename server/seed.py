from faker import Faker
from datetime import timedelta, datetime

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
    start_date = fake.date_time_this_year(
        after_now=True
    )  # Ensure start date is after today
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
    tasks = [
        {
            "title": "Book Flights",
            "note": "Find and book round-trip flights for the trip.",
            "link": "https://www.example.com/flights",
            "cost": 400.00,
            "optional": False,
            "everyone": True,
        },
        {
            "title": "Explore Local Cuisine",
            "note": "Try out local restaurants and food places.",
            "link": "https://www.example.com/local-cuisine",
            "cost": 0.00,
            "optional": True,
            "everyone": False,
        },
        {
            "title": "Visit Landmarks",
            "note": "Visit famous landmarks and tourist attractions.",
            "link": "https://www.example.com/landmarks",
            "cost": 50.00,
            "optional": False,
            "everyone": False,
        },
        # Add more tasks if needed
    ]

    for task_data in tasks:
        task = Task(
            trip=trip,
            title=task_data["title"],
            note=task_data["note"],
            link=task_data["link"],
            cost=task_data["cost"],
            optional=task_data["optional"],
            everyone=task_data["everyone"],
        )
        db.session.add(task)
    db.session.commit()


def create_fake_event(trip):
    events = [
        {
            "title": "Guided City Tour",
            "start_time": trip.start_date + timedelta(days=2, hours=10),
            "end_time": trip.start_date + timedelta(days=2, hours=12),
            "link": "https://www.example.com/city-tour",
            "ticketed": True,
            "price": 30.00,
            "note": "Join the city tour to explore the main attractions.",
        },
        {
            "title": "Beach Party",
            "start_time": trip.start_date + timedelta(days=5, hours=18),
            "end_time": trip.start_date + timedelta(days=5, hours=22),
            "link": "https://www.example.com/beach-party",
            "ticketed": False,
            "price": 0.00,
            "note": "Relax and enjoy a beach party with fellow travelers.",
        },
        {
            "title": "Art Gallery Visit",
            "start_time": trip.start_date + timedelta(days=3, hours=14),
            "end_time": trip.start_date + timedelta(days=3, hours=16),
            "link": "https://www.example.com/art-gallery",
            "ticketed": True,
            "price": 15.00,
            "note": "Explore local art at the city's renowned art gallery.",
        },
        # Add more events if needed
    ]

    for event_data in events:
        event = Event(
            trip=trip,
            title=event_data["title"],
            start_time=event_data["start_time"],
            end_time=event_data["end_time"],
            link=event_data["link"],
            ticketed=event_data["ticketed"],
            price=event_data["price"],
            note=event_data["note"],
        )
        db.session.add(event)
    db.session.commit()


def create_fake_travel_leg(trip, user):
    travel_leg_data = {
        "travel_type": fake.random_element(elements=("Departure", "Returning")),
        "departure_time": fake.date_time_this_year(after_now=True),
        "arrival_time": fake.date_time_this_year(after_now=True, before_now=False),
        "flight_number": fake.word(),
    }

    travel_leg = TravelLeg(
        trip=trip,
        user=user,
        travel_type=travel_leg_data["travel_type"],
        departure_time=travel_leg_data["departure_time"],
        arrival_time=travel_leg_data["arrival_time"],
        flight_number=travel_leg_data["flight_number"],
    )
    db.session.add(travel_leg)
    db.session.commit()


def create_fake_trip_lodging(trip):
    link = fake.url()
    note = "Stay at a comfortable and centrally located hotel."

    lodging = Lodging(trip=trip, link=link, note=note)
    db.session.add(lodging)
    db.session.commit()


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

        # Create 30 fake trips
        for _ in range(30):
            trip = create_fake_trip()

            # Add users to the trip as trip users
            for user in users:
                create_fake_trip_user(trip, user)

            # Create fake trip tasks
            create_fake_task(trip)

            # Create fake events
            create_fake_event(trip)

            # Create fake travel legs
            for user in users:
                create_fake_travel_leg(trip, user)

            # Create fake trip lodging
            create_fake_trip_lodging(trip)
