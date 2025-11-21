from app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(150), unique = True, nullable = False)
    email = db.Column(db.Integer, unique = True, nullable = False)
    password = db.Column(db.String(100), nullable = False)
    role = db.Column(db.String(50), nullable = False)
    created_at = db.Column(db.DateTime , default = datetime.now)

    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'), nullable = True)

    dep = db.relationship('departments', back_populates = 'doc')

class Department(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), unique = True, nullable = False)
    description = db.Column(db.Text, nullable = True)
    
    doc =  db.relationship('departments', back_populates = 'dep')

class Appointmnet(db.Model):
    __tablename__ = 'appointment'

    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.String(50))
    time = db.Column(db.String(50))
    status = db.Column(db.String(30), default = 'Booked')
    

