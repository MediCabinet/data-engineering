# web_app/routes/home_routes.py

from flask import Blueprint, jsonify

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    return jsonify("Hello World! This should be the home route.")

@home_routes.route("/strain/<int:n>")
def strain_list():
    return jsonify(f"")