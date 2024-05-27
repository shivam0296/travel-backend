from flask import Flask, jsonify, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import datetime
import pymysql
from flask_marshmallow import Marshmallow
import requests
from mqtt_com import SearchTrip, SearchTour, AddTrip, ClearTrip
from clear_trip import MqttClear
from flask_cors import CORS
pymysql.install_as_MySQLdb()

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///students.sqlite3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
app.app_context().push()
ma = Marshmallow(app)


class Trips(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(200))
    lastname = db.Column(db.String(200))
    source = db.Column(db.String(200))
    destination = db.Column(db.String(200))
    datecreated = db.Column(db.DateTime, default = datetime.datetime.now())

    def __init__(self, firstname, lastname, source, destination):
        self.firstname = firstname
        self.lastname = lastname
        self.source = source
        self.destination = destination


class TripSchema(ma.Schema):
    class Meta:
        fields = ('id', 'firstname', 'lastname', 'source', 'destination', 'datecreated')

trip_schema = TripSchema()
trips_schema = TripSchema(many=True)

@app.route('/get', methods=['GET'])
def get_trips():
    all_trips = Trips.query.all()
    results = trips_schema.dump(all_trips)
    return jsonify(results)

@app.route('/get/<id>/', methods=['GET'])
def get_trip(id):
    trip = Trips.query.get(id)
    result = trip_schema.jsonify(trip)
    return result

@app.route('/add', methods=['POST'])
def add_trips():
    firstname = request.json['firstname']
    lastname = request.json['lastname']
    source = request.json['source']
    destination = request.json['destination']
    mqtt_add = AddTrip(lastname, firstname+" "+lastname, source, destination)
    trip = Trips(firstname, lastname, source, destination)
    db.session.add(trip)
    db.session.commit()
    mqtt_add.run()
    return trip_schema.jsonify(trip)

@app.route('/update/<id>/', methods=['PUT'])
def update_trip(id):
    trip = Trips.query.get(id)
    firstname = request.json['firstname']
    lastname = request.json['lastname']
    source = request.json['source']
    destination = request.json['destination']
    
    trip.firstname = firstname 
    trip.lastname = lastname
    trip.source = source
    trip.destination = destination
    
    db.session.commit()

    return trip_schema.jsonify(trip)

@app.route('/delete/<id>/', methods=['DELETE'])
def delete_trips(id):
    trip = Trips.query.get(id)
    db.session.delete(trip)
    db.session.commit()

    return trip_schema.jsonify(trip)

@app.route('/mqttsearch', methods=['GET'])
def mqtt_search_trips():
    mqtt_trips = SearchTrip()
    res = mqtt_trips.run()
    return jsonify(res)

@app.route('/toursearch', methods=['GET'])
def mqtt_tour_trips():
    tour_trips = SearchTrip()
    res = tour_trips.run()
    return jsonify(res)

@app.route('/mqttclear', methods=['GET'])
def mqtt_clear():
    clear_trips = MqttClear()
    res = clear_trips.run()
    return jsonify({'Action': ' Trips Cleared Successfully'}) if res else jsonify({'Action': 'Could not clear Trips'})

@app.route('/location', methods=['POST'])
def get_location():
    if request.method == 'POST':
        location = request.json['location']
        return redirect(url_for('location_trips', location=location))
    
@app.route('/location_trips', methods=['GET'])
def location_trips():
    loc = get_curr_location()
    loc = loc.split(',')[-2].strip()
    result = db.session.query(Trips).filter(Trips.source == loc).all()
    data = [{'firstname': res.firstname, 
             'lastname': res.lastname, 
             'source':res.source, 
             'destination':res.destination, 
             'datecreated': res.datecreated,
             'id': res.id} for res in result]
    mq_search = SearchTrip(loc)
    res = mq_search.run()
    print(res)
    return jsonify(data)

def get_curr_location():
    # Get user's current location coordinates using Geolocation API
    response = requests.get('https://ipinfo.io/json')
    data = response.json()
    lat, lon = data['loc'].split(',')

    # Reverse geocode the coordinates to get the location name
    api_key = 'c6e3c9905f104ecf8514cf640a9cfe32'
    url = f'https://api.opencagedata.com/geocode/v1/json?q={lat}+{lon}&key={api_key}&language=en'
    response = requests.get(url)
    data = response.json()
    location_name = data['results'][0]['formatted']
    return location_name

@app.route('/curr_location', methods=['GET'])
def curr_location():
    res = get_curr_location()
    loc = res.split(',')[-2].strip()
    return jsonify({'curr': loc})

@app.route('/guide', methods=['GET'])
def get_gtrips():
    loc = get_curr_location()
    loc = loc.split(',')[-2].strip()
    result = db.session.query(Trips).filter(Trips.destination == loc).all()
    data = [{'firstname': res.firstname, 
             'lastname': res.lastname,
             'source':res.source, 
             'destination':res.destination, 
             'datecreated': res.datecreated,
             'id': res.id} for res in result]
    mq_search = SearchTrip(loc)
    res = mq_search.run()
    print(res)
    return jsonify(data)


if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()
    #     print("created db")
    app.run()
    
