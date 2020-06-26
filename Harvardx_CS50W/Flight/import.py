import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from models import *
from settings import *

engine = create_engine(DATABASE_URI)
db = scoped_session(sessionmaker(bind=engine))

if __name__ == "__main__":
    with open("flights.csv", "r") as f:
        reader = csv.reader(f)
        for o, dest, dur in reader:
            flight = Flight(origin=o, destination=dest, duration=dur)
            db.add(flight)
            db.commit()
