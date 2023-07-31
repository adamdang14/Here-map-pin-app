from flask import Flask, request, jsonify, render_template,  redirect, flash, session
from models import db, connect_db, Pin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tvksqwlv:iGIaXrY2bSMe0JAv_3p_l3mHYuOYZDoB@stampy.db.elephantsql.com/tvksqwlv'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True


connect_db(app)

@app.route('/')
def index():
    pins = Pin.query.all()
    return render_template('form.html', pins=pins)

@app.route('/', methods=['POST'])
def submit_pin():
    # data = request.get_json()
    latitude = request.form['latitude']
    longitude = request.form['longitude']
    title = request.form['title']
    description = request.form['description']

    new_pin = Pin(latitude=latitude, longitude=longitude, title=title, description=description)
    db.session.add(new_pin)
    db.session.commit()

    # return jsonify({'message': 'Pin submitted successfully!'}), 201
    return redirect('/')

@app.route('/pins', methods=['GET'])
def get_pins():
    pins = Pin.query.all()
    pin_data = [{'latitude': pin.latitude, 'longitude': pin.longitude, 'title': pin.title, 'description': pin.description} for pin in pins]

    return jsonify(pin_data)

if __name__ == '__main__':
    app.run(debug = True)   
