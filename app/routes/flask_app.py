# app/routes/flask_app.py

# import packages
from flask import Blueprint, jsonify
from app.models import db, Database, parse_records


flask_app = Blueprint("flask_app", __name__)


@flask_app.route("/")
def home():
    hello = "Hello World!"
    return jsonify(hello)


@flask_app.route("/about")
def about():
    return jsonify("About me")


@flask_app.route("/strain")
def strain_id():
    db_database = Database.query.all()
    strain_response = parse_records(db_database)
    return jsonify(strain_response)


