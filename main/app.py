from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(150), unique = True, nullable = False)
    email = db.Column(db.String(150), unique = True, nullable = False)
    password = db.Column(db.String(100), nullable = False)
    role = db.Column(db.String(50), nullable = False)
    created_at = db.Column(db.DateTime , default = datetime.now)

    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'), nullable = True)

    dep = db.relationship('Department', back_populates = 'users')
    appointments = db.relationship("Appointment", back_populates = 'user')

class Department(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), unique = True, nullable = False)
    description = db.Column(db.Text, nullable = True)
    
    users =  db.relationship('User', back_populates = 'dep')

class Appointment(db.Model):
    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.String(50))
    time = db.Column(db.String(50))
    status = db.Column(db.String(30), default = 'Booked')
    
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    treatment_id = db.Column(db.Integer, db.ForeignKey("treatments.id"), unique = True)
    
    user = db.relationship("User", back_populates = "appointments")
    
class Treatment(db.Model):
    __tablename__ = "treatments"

    id = db.Column(db.Integer, primary_key = True)
    treat_name = db.Column(db.String(100))
    description = db.Column(db.Text)

if __name__ == '__main__':
    with app.app_context():
      db.create_all()
      existing_admin = User.query.filter_by(username = 'admin').first()

      if not existing_admin:
        admin_db = User(
            username = 'admin',
            password = 'admin',
            email = "ad123@gmail.com",
            role = "admin"
        )
        db.session.add(admin_db)
        db.session.commit()

    app.run(debug=True)  