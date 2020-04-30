# Med Cabinet Strain Recommender API

Small back-end Flask API model providing marijuana strain recommendations for the Med Cabinet project, based on desired effects and ailments to be treated.


## Deployment


### Running Flask app locally:

```sh
# Unix:
FLASK_APP = app flask run

# Windows:
export FLASK_APP = app  # one-time thing, to set the env var
flask run
```

### Migrate the db:

```sh
FLASK_APP = app flask db init
FLASK_APP = app flask db migrate
FLASK_APP = app flask db upgrade
```

### Local Environment Access:

`http://127.0.0.1:5000/`


### Running Flask app on heroku:

```sh
heroku login
```

Creating a new application server (MUST BE DONE FROM WITHIN THE REPOSITORY'S ROOT DIRECTORY):

```sh
git remote -v
heroku create # optionally provide a name... "heroku create medi-cabinet"
git remote -v
```

Deploying to production:

```sh
git push heroku master
# or... git push heroku my_branch:master
```

Viewing production app in browser:

```sh
heroku open
```

Checking production server logs:

```sh
heroku logs --tail

Provisioning production database:

```sh
heroku config
heroku addons:create heroku-postgresql:hobby-dev
#> provisions a new DATABASE_URL
heroku config
```

Migrating the production database:

```sh
# first login to the server, then run the migration commands there:
heroku run bash
# ... FLASK_APP=web_app flask db init
# ... FLASK_APP=web_app flask db migrate
# ... FLASK_APP=web_app flask db upgrade

# that should work, but alternatively you might be able to run these detached commands (if you didn't ignore your migrations dir):
heroku run "FLASK_APP=app flask db init"
heroku run "FLASK_APP=app flask db stamp head"
heroku run "FLASK_APP=app flask db migrate"
heroku run "FLASK_APP=app flask db upgrade"
```

# Usage

### Raw data output

There are 3 endpoints returning raw tables from the postgreSQL DB:

    /base # raw output from base table

    /strain # raw output from strain table

    /template # raw output from template 

**Parameters:** None

**Returns:** JSON array containing available strain information

Example: ```sh
https://medi-cabinet.herokuapp.com/base 

https://medi-cabinet.herokuapp.com/strain 

https://medi-cabinet.herokuapp.com/template```


### Recommended Strains

Endpoint to return a list of recommendations.

    /recommend

**Parameters:** 
Passing a `POST` request to the endpoint with an JSON object that looks like:
```
 {
        "effects":["happy", "euphoric", "creative"],
        "ailments":["anxiety", "depression", "pain"],
        "negatives":["dry mouth", "paranoid", "dizzy"]
    }
```

**Returns:** JSON array containing strain `id` and `n` recommendations.

Example:
```json
[
    {
        "id": "72"
    },
    {
        "id": "0"
    },
    {
        "id": "33"
    },
    {
        "id": "169"
    },
    {
        "id": "988"
    },
    {
        "id": "403"
    },
    {
        "id": "55"
    },
    {
        "id": "390"
    },
    {
        "id": "881"
    },
    {
        "id": "683"
    }
]
```

### Testing

```
TODO
```

## Project Information

[Product Vision Document](https://docs.google.com/document/d/1PNvyYa1qH1uxq-YKAhYnAPhT5jSBBE3XgYDzgQpFIUE/edit#heading=h.p0mtiic9v46n)

[Med Cabinet Project Pitch and Rubrics](https://www.notion.so/Med-Cabinet-7960b90bb485430483bb266f7b738308)