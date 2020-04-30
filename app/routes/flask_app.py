# app/routes/flask_app.py

# import packages
from flask import Blueprint, jsonify, request, render_template
from app.models import db, Base, Strain, parse_records


flask_app = Blueprint("flask_app", __name__)


@flask_app.route("/")
def home():
    hello = "Hello World!"
    return jsonify(hello)


@flask_app.route("/about")
def about():
    return jsonify("About me")


@flask_app.route("/base")
def base():
    db_base = Base.query.all()
    base_response = parse_records(db_base)
    return jsonify(base_response)


@flask_app.route("/strain")
def strain():
    db_strain = Strain.query.all()
    strain_response = parse_records(db_strain)
    return jsonify(strain_response)


