from datetime import datetime
from medical import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(400), nullable=False)
    gender = db.Column(db.String(5), nullable=False)

    def __repr__(self):
        return f"User('{self.name}', '{self.email}', '{self.image_file}', '{self.age}')"


class MedicalHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, nullable=False, unique=True)
    doctor_id = db.Column(db.Integer, nullable=False, unique=True)
    heading = db.Column(db.String(200), nullable=False)
    uploaded_file = db.Column(db.String(200), nullable=False)
    patient_notes = db.Column(db.String(1000), default=" ")
    doctor_remarks = db.Column(db.String(1000), default=" ")
    date_of_report = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)
    doctor_name = db.Column(db.String(30), nullable=False)
