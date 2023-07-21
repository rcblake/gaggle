from config import db, app
from models import User, Trip, TripUser


# Function to add a user to a trip
def add_user_to_trip(user, trip):
    trip_user = TripUser(trip=trip, user=user)
    db.session.add(trip_user)
    db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        # Assuming you have already run the seed file and created the users and trips
        # Retrieve user with id 6
        user_id_to_add = 6
        user = User.query.get(user_id_to_add)

        # Retrieve all trips
        trips = Trip.query.all()

        # Add the user to the first 10 trips
        for trip in trips[:10]:
            add_user_to_trip(user, trip)
