# web_app/routes/result_routes.py

from flask import Blueprint, jsonify

cannabis_routes = Blueprint("cannabis_routes", __name__)

@cannabis_routes.route("/prediction")
def index():
    return jsonify(f"You should see what you are looking for here.")