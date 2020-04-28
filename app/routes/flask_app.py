# app/routes/flask_app.py

# import packages
from flask import Blueprint, jsonify

flask_app = Blueprint("flask_app", __name__)

@flask_app.route("/")
def home():
    hello = "Hello World!"
    return jsonify(hello)


@flask_app.route("/about")
def about():
    return jsonify("About me")

