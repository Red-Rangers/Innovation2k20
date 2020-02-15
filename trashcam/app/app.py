from flask import Flask,render_template,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from config import Config
from get_dummy_coordinates import get_points
from bucket import multi_part_upload
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

UPLOAD_FOLDER = os.path.join('static','images')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.before_first_request
def init():
    db.create_all()
     
class Uploads(db.Model):
    __tablename__ = 'uploads'
    ids = db.Column(db.Integer,primary_key=True)
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

@app.route('/camera')
def camera():
    return render_template('camera.html')

@app.route('/coord')
def coord():
    return render_template('geocoord.html')

@app.route('/submit',methods=['POST'])
def submit():
    if 'camera_input' not in request.files:
        return 'no input'
    lat = request.form['lat']
    longi = request.form['long']
    id = Uploads.query.count()
    id=id+1
    print(id,lat,longi)
    entry = Uploads(ids=id,latitude=lat,longitude=longi) 
    db.session.add(entry)
    db.session.commit()
    file = request.files['camera_input']
    img_src = os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(file.filename))
    file.save(img_src)
    multi_part_upload(file.filename,img_src) 
    return 'thank you! successfully uploaded'

@app.route('/map')
def map():
    return render_template('map.html')

#api calls

@app.route('/api/points')
def get_points():
    dat = db.engine.execute("select latitude,longitude from uploads")   
    coord = [{"lat":x[0],"long":x[1]} for x in dat]
    print(coord)
    return jsonify(coord)



if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)

