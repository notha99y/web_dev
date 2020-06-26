from flask import Flask, jsonify, render_template, request

from models import *
from settings import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@app.route("/")
def index():
    flights = Flight.query.all()
    return render_template("index.html", flights=flights)


@app.route("/book", methods=["POST"])
def book():
    """Book a flight"""

    name = request.form.get("name")
    try:
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("error.html", message="Invalid flight number.")

    flight = Flight.query.get(flight_id)

    if flight is None:
        return render_template(
            "error.html", message="No such flight with that id"
        )
    flight.add_passenger(name)
    return render_template("success.html")


@app.route("/flights")
def flights():
    """List all flights"""
    flights = Flight.query.all()
    return render_template("flights.html", flights=flights)


@app.route("/flights/<int:flight_id>")
def flight(flight_id):
    flight = Flight.query.get(flight_id)
    if flight is None:
        return render_template("error.html", message="No such flight")

    passengers = flight.passengers
    return render_template("flight.html", flight=flight, passengers=passengers)


@app.route("/api/flights/<int:flight_id>")
def flight_api(flight_id):
    """Return details about a single flight"""
    flight = Flight.query.get(flight_id)
    if flight is None:
        return jsonify({"error": "Invalid flight id"}), 422

    passengers = flight.passengers
    names = []
    for passenger in passengers:
        names.append(passenger.name)

    return jsonify(
        {
            "origin": flight.origin,
            "destination": flight.destination,
            "duration": flight.duration,
            "passengers": names,
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5050")
