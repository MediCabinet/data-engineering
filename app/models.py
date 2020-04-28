# app/models.py

# import packages
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

migrate = Migrate()

class Database(db.Model):
    strain_id = db.Column(db.Integer, primary_key=True)
    happy = db.Column(db.String)
    hungry = db.Column(db.String)
    relaxed = db.Column(db.String)
    sleepy = db.Column(db.String)
    anxious = db.Column(db.String)
    depression = db.Column(db.String)
    fatigue = db.Column(db.String)
    headaches = db.Column(db.String)
    pain = db.Column(db.String)
    stress = db.Column(db.String)
    dry eyes
    dry mouth
    
    


def parse_records(database_records):
    """
    A helper method for converting a list of database record objects into a list of dictionaries, so they can be returned as JSON

    Param: database_records (a list of db.Model instances)

    Example: parse_records(User.query.all())

    """
    parsed_records = []
    for record in database_records:
        print(record)
        parsed_record = record.__dict__
        del parsed_record["_sa_instance_state"]
        parsed_records.append(parsed_record)
    return parsed_records
