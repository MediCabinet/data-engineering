# web_app/models.py

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pandas as pd

db = SQLAlchemy()
migrate = Migrate()

class Module(db.Model):
    """Model database class"""
    anxious = db.Column(db.String(128), nullable=False)
    dizzy = db.Column(db.String(128), nullable=False)
    paranoid = db.Column(db.String(128), nullable=False)
    dizzy = db.Column(db.String(128), nullable=False)
    dry_eyes = db.Column(db.String(128), nullable=False)
    dry_mouth = db.Column(db.String(128), nullable=False)
    headache = db.Column(db.String(128), nullable=False)
    paranoid = db.Column(db.String(128), nullable=False)
    creative = db.Column(db.String(128), nullable=False)
    energetic = db.Column(db.String(128), nullable=False)
    euphoric = db.Column(db.String(128), nullable=False)
    focused = db.Column(db.String(128), nullable=False)
    happy = db.Column(db.String(128), nullable=False)
    relaxed = db.Column(db.String(128), nullable=False)
    sleepy = db.Column(db.String(128), nullable=False)
    anxiety = db.Column(db.String(128), nullable=False)
    depression = db.Column(db.String(128), nullable=False)
    fatigue = db.Column(db.String(128), nullable=False)
    headaches = db.Column(db.String(128), nullable=False)
    lack_of_appetite = db.Column(db.String(128), nullable=False)
    pain = db.Column(db.String(128), nullable=False)
    stress = db.Column(db.String(128), nullable=False)
    strain_id = db.Column(DB.Integer, primary_key=True)
    
    def __repr__(self):
        output = {
            'id':self.index,
            'name':self.Strain,
            'type':self.Type,
            'rate':self.Rating,
            'desc':self.Description,
            'flavor':self.flavors,
            'medical':self.medical,
            'positive':self.positive,
            'negative':self.negative
        }
        return output

    def __str__(self):
        return self.__repr__()
    
    
    
    
    
    
    
    
    
    
    
    
    
    

def parse_records(database_records):
    """
    A helper method for converting a list of database record objects into a list of dictionaries, so they can be returned as JSON

    Param: database_records (a list of db.Model instances)

    Example: parse_records(User.query.all())

    Returns: a list of dictionaries, each corresponding to a record, like...
        [
            {"id": 1, "title": "Book 1"},
            {"id": 2, "title": "Book 2"},
            {"id": 3, "title": "Book 3"},
        ]
    """
    parsed_records = []

    for record in database_records:
        print(record)
        parsed_record = record.__dict__
        del parsed_record["_sa_instance_state"]
        parsed_records.append(parsed_record)

    return parsed_records