from flask import Flask,render_template,jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config
from get_dummy_coordinates import get_points
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

@app.before_first_request
def init():
    db.create_all()
     
class User(db.Model):
    __tablename__ = 'user'
    username = db.Column(db.String(50),primary_key=True,nullable=False)
   
class Uploads(db.Model):
    __tablename__ = 'uploads'
    id = db.Column(db.Integer,primary_key=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/maps')
def maps():
    return render_template('maps.html')

@app.route('/geo')
def geo():
    return render_template('geo.html')

#api calls

@app.route('/api/points')
def get_points():
    coord = [{'lat': '13.217096', 'long': '79.100677'}, {'lat': '13.752690', 'long': '79.703758'}, {'lat': '22.671679', 'long': '88.300209'}, {'lat': '28.627926', 'long': '79.804176'}, {'lat': '20.927933', 'long': '79.004143'}, {'lat': '19.846811', 'long': '75.890633'}, {'lat': '29.257648', 'long': '78.500061'}, {'lat': '24.571270', 'long': '73.691544'}, {'lat': '30.923433', 'long': '74.610214'}, {'lat': '16.538591', 'long': '80.798218'}, {'lat': '19.465622', 'long': '72.806099'}, {'lat': '22.308155', 'long': '70.800705'}, {'lat': '26.651218', 'long': '92.783813'}, {'lat': '11.748050', 'long': '75.489380'}, {'lat': '20.903118', 'long': '74.774986'}, {'lat': '30.087160', 'long': '78.268112'}, {'lat': '29.162411', 'long': '79.152168'},{'lat': '19.432278', 'long': '72.774300'}, {'lat': '22.572645', 'long': '88.363892'}, {'lat': '28.984644', 'long': '77.705956'}]
    return jsonify(coord)
    

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)

