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
    return jsonify(coord)

@app.route('/api/points2')
def get_p():
    coord = [{'lat': '12.120000', 'long': '76.680000'}, {'lat': '24.879999', 'long': '74.629997'}, {'lat': '16.994444', 'long': '73.300003'}, {'lat': '19.155001', 'long': '72.849998'}, {'lat': '24.794500', 'long': '73.055000'}, {'lat': '21.250000', 'long': '81.629997'}, {'lat': '16.166700', 'long': '74.833298'}, {'lat': '26.850000', 'long': '80.949997'}, {'lat': '28.610001', 'long': '77.230003'}, {'lat': '19.076090', 'long': '72.877426'}, {'lat': '14.167040', 'long': '75.040298'}, {'lat': '26.540457', 'long': '88.719391'}, {'lat': '24.633568', 'long': '87.849251'}, {'lat': '28.440554', 'long': '74.493011'}, {'lat': '24.882618', 'long': '72.858894'}, {'lat': '16.779877', 'long': '74.556374'}, {'lat': '12.715035', 'long': '77.281296'}, {'lat': '13.432515', 'long': '77.727478'}, {'lat': '12.651805', 'long': '77.208946'}, {'lat': '22.728392', 'long': '71.637077'}, {'lat': '9.383452', 'long': '76.574059'}, {'lat': '14.623801', 'long': '75.621788'}, {'lat': '10.925440', 'long': '79.838005'}, {'lat': '15.852792', 'long': '74.498703'}, {'lat': '19.354979', 'long': '84.986732'}, {'lat': '23.905445', 'long': '87.524620'}, {'lat': '20.296059', 'long': '85.824539'}, {'lat': '21.105001', 'long': '71.771645'}, {'lat': '30.172716', 'long': '77.299492'}, {'lat': '25.477585', 'long': '85.709091'}, {'lat': '21.045521', 'long': '75.801094'}, {'lat': '26.491890', 'long': '89.527100'}, {'lat': '8.893212', 'long': '76.614143'}, {'lat': '22.430889', 'long': '87.321487'}, {'lat': '23.849325', 'long': '72.126625'}, {'lat': '11.786253', 'long': '77.800781'}, {'lat': '13.583274', 'long': '76.540154'}, {'lat': '14.530457', 'long': '75.801094'}, {'lat': '18.901457', 'long': '73.176132'}, {'lat': '22.960510', 'long': '88.567406'}, {'lat': '15.756595', 'long': '76.192696'}, {'lat': '22.656015', 'long': '86.352882'}, {'lat': '25.989836', 'long': '79.450035'}, {'lat': '23.223047', 'long': '82.870560'}, {'lat': '19.186354', 'long': '73.191948'}, {'lat': '30.525005', 'long': '75.890121'}, {'lat': '22.422455', 'long': '85.760651'}, {'lat': '18.106659', 'long': '83.395554'}, {'lat': '21.190449', 'long': '81.284920'}, {'lat': '23.597969', 'long': '72.969818'}, {'lat': '28.590361', 'long': '78.571762'}, {'lat': '25.369179', 'long': '85.530060'}, {'lat': '11.623377', 'long': '92.726486'}, {'lat': '24.618393', 'long': '88.024338'}, {'lat': '23.546757', 'long': '74.433830'}, {'lat': '41.643414', 'long': '41.639900'}, {'lat': '25.077787', 'long': '87.900375'}, {'lat': '29.854263', 'long': '77.888000'}, {'lat': '14.913181', 'long': '79.992981'}, {'lat': '14.413745', 'long': '77.712616'}, {'lat': '18.101904', 'long': '78.852074'}, {'lat': '23.173939', 'long': '81.565125'}, {'lat': '15.812074', 'long': '80.355377'}, {'lat': '15.764501', 'long': '79.259491'}, {'lat': '10.311879', 'long': '76.331978'}, {'lat': '21.961946', 'long': '70.792297'}, {'lat': '16.544893', 'long': '81.521240'}, {'lat': '21.049540', 'long': '76.532028'}, {'lat': '26.182245', 'long': '91.754723'}, {'lat': '27.897551', 'long': '77.384117'}, {'lat': '18.245655', 'long': '76.505356'}, {'lat': '23.486839', 'long': '75.659157'}, {'lat': '32.041943', 'long': '75.405334'}, {'lat': '24.474380', 'long': '85.688744'}, {'lat': '23.427221', 'long': '87.287018'}, {'lat': '19.487707', 'long': '75.380768'}, {'lat': '19.853060', 'long': '74.000633'}, {'lat': '15.167409', 'long': '77.373627'}, {'lat': '24.417534', 'long': '88.250343'}, {'lat': '22.744108', 'long': '77.736969'}, {'lat': '14.752805', 'long': '78.552757'}, {'lat': '23.520399', 'long': '87.311897'}, {'lat': '25.771315', 'long': '73.323685'}, {'lat': '28.148735', 'long': '77.332024'}, {'lat': '29.138407', 'long': '76.693245'}, {'lat': '25.375710', 'long': '86.474373'}, {'lat': '20.388794', 'long': '78.120407'}, {'lat': '23.669296', 'long': '86.151115'}, {'lat': '21.761524', 'long': '70.627625'}, {'lat': '22.657402', 'long': '88.867180'}, {'lat': '22.700474', 'long': '88.319069'}, {'lat': '23.344101', 'long': '85.309563'}, {'lat': '14.146319', 'long': '79.850388'}, {'lat': '28.078636', 'long': '80.471588'}, {'lat': '27.108416', 'long': '78.584602'}, {'lat': '9.823619', 'long': '77.986565'}, {'lat': '12.946366', 'long': '79.959244'}, {'lat': '17.143908', 'long': '79.623924'}, {'lat': '13.340881', 'long': '74.742142'}, {'lat': '15.478569', 'long': '78.483093'}]
    return jsonify(coord)


if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)

