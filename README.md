# Installation

TODO: instructions

# Setup

TODO: instructions BLAH BLAH

Running flask app:
```
FLASK_APP = app flask run
```

Migrate the db:

```sh
FLASK_APP = app flask db init
FLASK_APP = app flask db migrate
FLASK_APP = app flask db upgrade
```

# Usage

```sh
# Unix:
FLASK_APP = app flask run

# Windows:
export FLASK_APP = app  # one-time thing, to set the env var
flask run


Heroku URL:
https://medi-cabinet.herokuapp.com/base # raw output from base table
https://medi-cabinet.herokuapp.com/strain # raw output from strain table
https://medi-cabinet.herokuapp.com/template # raw output from template table
https://medi-cabinet.herokuapp.com/recommend # predictions output from model. This is the enpoint you need to hit with that json object.



DATABASE_URL:
postgres://nssinfmkbdjqiv:8c8f6ed0ccef41cd2b9fc0641056770a7fdaec8973bc9f77927b2c9c24092b57@ec2-54-152-175-141.compute-1.amazonaws.com:5432/d4f3qq064sot52

```
