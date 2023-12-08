from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
import string, datetime

metadata = MetaData(
    naming_convention={
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    }
)
db = SQLAlchemy(metadata=metadata)

class Patient(db.Model, SerializerMixin):
    __tablename__ = "patient_table"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)





class Appointment(db.Model, SerializerMixin):
    __tablename__ = "appointment_table"

    id = db.Column(db.Integer, primary_key = True)
    day = db.Column(db.String, nullable = False)
    doctor_id = db.Column(db.Integer, db.ForeignKey("doctor_table.id"), nullable = False)
    patient_id = db.Column(db.Integer, db.ForeignKey("patient_table.id"), nullable = False)
    
    @validates('day')
    def validates_name(self, key: str, value: str):
        if value in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
            return value
        else:
            raise ValueError('Invalid Weekday')


class Doctor(db.Model, SerializerMixin):
    __tablename__ = "doctor_table"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    specialty = db.Column(db.String, nullable = False)

    @validates('name')
    def validates_name(self, key: str, value: str):
        if value[0:4] == 'Dr. ':
            return value
        else:
            raise ValueError('Name must begin with "Dr. "')
