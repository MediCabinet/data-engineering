# app/models.py

# import packages
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

migrate = Migrate()

# class Base(db.Model):
#     strain_id = db.Column(db.Integer, primary_key=True)
#     stress = db.Column(db.Integer)
#     pain = db.Column(db.Integer)
#     lack_of_appetite = db.Column(db.Integer)
#     headaches = db.Column(db.Integer)
#     fatigue = db.Column(db.Integer)
#     depression = db.Column(db.Integer)
#     anxiety = db.Column(db.Integer)
#     sleepy = db.Column(db.Integer)
#     relaxed = db.Column(db.Integer)
#     hungry = db.Column(db.Integer)
#     happy = db.Column(db.Integer)
#     focused = db.Column(db.Integer)
#     euphoric = db.Column(db.Integer)
#     energetic = db.Column(db.Integer)
#     creative = db.Column(db.Integer)
#     paranoid = db.Column(db.Integer)
#     headache = db.Column(db.Integer)
#     dry_mouth = db.Column(db.Integer)
#     dry_eyes = db.Column(db.Integer)
#     dizzy = db.Column(db.Integer)
#     anxious = db.Column(db.Integer)
    

# class Strain(db.Model):
#     strain_id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     type = db.Column(db.String)
#     rating = db.Column(db.Integer)
    

# class Template(db.Model):
#     """Template database class"""
#     strain_id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String, nullable=False)
#     type = db.Column(db.String, nullable=False)
#     rating = db.Column(db.Integer, nullable=False)
#     effects = db.Column(db.String, nullable=False)
#     flavor = db.Column(db.String, nullable=False)
#     description = db.Column(db.String, nullable=False)


class Cabinet(db.Model):
    """Table database class"""
    strain_id = db.Column(db.Integer, primary_key=True)
    strain_name = db.Column(db.String)
    strain_type = db.Column(db.String)
    strain_rating = db.Column(db.String)
    effects_profile = db.Column(db.String)
    flavor_profile = db.Column(db.String)
    strain_description = db.Column(db.String)
    model_id = db.Column(db.Integer)

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
