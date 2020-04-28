# web_app/__init__.py

#
#> $env:FLASK_APP = "web_app" #> flask run
#

# import packages
import os
from dotenv import load_dotenv
from flask import Flask

# Import routes
from web_app.models import db, migrate
from web_app.routes.home_routes import home_routes
from web_app.routes.cannabis_routes import cannabis_routes

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


# application factory pattern
def create_app():
    app = Flask(__name__)

    # configure the database
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # supress warning messages

    db.init_app(app)
    migrate.init_app(app, db)

    # configure routes
    app.register_blueprint(home_routes)
    app.register_blueprint(cannabis_routes)

    return app


if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)