# app/routes/flask_app.py

# import packages
from flask import Blueprint, jsonify, render_template, request
from app.models import db, Base, Strain, Template, parse_records


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


# @flask_app.route("/strain/qa_form")
# def strain_model_form():
#     return render_template("qa_form.html")


# @flask_app.route("/strain/output", methods=["POST"])
# def strain_model_input():
#     effect_dict = request.form.getlist("effect_list")
#     negative_dict = request.form.getlist("negative_list")
#     ailments_dict = request.form.getlist("ailment_list")
	
#     dict_of_inputs = {"effects": effect_dict, 
#                       "negatives": negative_dict,
#                       "ailments": ailments_dict
#                 }

#     return dict_of_inputs


# @home_routes.route("/strain/result")
# def strain_kelly_model():

#     return jsonify(dict_of_inputs)

