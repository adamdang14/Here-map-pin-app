from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


class Pin(db.Model):
    __tablename__ = 'pins'
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    latitude = db.Column(db.Float, 
                         nullable=False)
    
    longitude = db.Column(db.Float, 
                          nullable=False)
    
    title = db.Column(db.String(100), 
                      nullable=False)
    
    description = db.Column(db.String(200), 
                            nullable=False)
