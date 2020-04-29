# web_app/routes/home_routes.py

from flask import Blueprint, jsonify
from web_app.models import db, Strain, parse_records
import pandas as pd

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    return jsonify("Hello World! This should be the home route.")

# @home_routes.route("/base")
# def base():
#     db_base = Base.query.all()
#     base_response = parse_records(db_base)
#     return jsonify(base_response)

# @home_routes.route("/strain/<int:n>")
# def strain():
#     records = parse_records(Strain.query.filter(Strain.strain_id == n).all())
#     return jsonify(records)

@home_routes.route("/strain/<int:n>")
def strain_single(n=None):
    records = parse_records(Strain.query.filter(Strain.strain_id == n).all())
    return jsonify(records)





@home_routes.route("/strain/<list>")
def strain_list(list):

    list = [3534,3536,3538,3554]
    records = []

    for i in list:
        records.append(parse_records(Strain.query.filter(Strain.strain_id == i).all()))

    return jsonify(records)

# def strain():
#     query = Strain.query.all()
#     return query

# \@home_routes.route("/strain")
# def strain():
#     db_strain = Strain.query.all()
#     strain_response = parse_records(db_strain)
#     return jsonify(records)