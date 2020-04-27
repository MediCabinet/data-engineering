# app/routes/flask_app.py

# import packages
from flask import Blueprint

flask_app = Blueprint("flask_app", __name__)

@flask_app.route("/")
def home():
    return f"Hello World!"
