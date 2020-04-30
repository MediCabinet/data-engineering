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
# ... FLASK_APP=app flask db init
# ... FLASK_APP=app flask db migrate
# ... FLASK_APP=app flask db upgrade

# that should work, but alternatively you might be able to run these detached commands (if you didn't ignore your migrations dir):
heroku run "FLASK_APP=app flask db init"
heroku run "FLASK_APP=app flask db stamp head"
heroku run "FLASK_APP=app flask db migrate"
heroku run "FLASK_APP=app flask db upgrade"
```

# Usage

### Raw data output

Endpoint returning raw tables from the postgreSQL DB:

    /cabinet # raw output from cabinet table

**Parameters:** None

**Returns:** JSON array containing available strain information

Example: 
`https://medi-cabinet.herokuapp.com/cabinet` 



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

## Model

Machine Learning model to recommend cannabis strains based on user input.

FUll documentation and data and source files on the model can be found here:
[ml-engineering](https://github.com/MediCabinet/ml-engineering)

### DATA
Sources:
* [Kushy API](https://raw.githubusercontent.com/kushyapp/cannabis-dataset/master/Dataset/Strains/strains-kushy_api.2017-11-14.csv)
    * Provides chemical composition of strains
* [Kaggle/Leafly](https://www.kaggle.com/kingburrito666/cannabis-strains)
    * Provides strain name, type, rating, effects, taste, and description
* Data Scraped from [Leafly](leafly.com)
    * Provides a rating for each strain regarding specific ailments, negative side effects, and postive effects a user may want to take into account

### MACHINE LEARNING MODEL
K-Nearest-Neighbor model takes a pandas series holding user input regarding their cannabis strain preferences and what is most important to them, and outputs a list of its nearest neighbors - most similar strains.

Inputs: 
 * Type of strain a user is looking for (hybrid, indica, sativa)
 * Desired effects (creative, energetic, euphoric, focused, happy, hungry)
 * Ailments they may be looking for relief from (anxiety, depression, fatigue, headaches, lack of appetite, pain, stress)
 * Negative side effects they are trying to avoid (anxious, dizzy, dry eyes, dry mouth, headache, paranoid)


### Testing
Flask API functionality was verified using Postman.


## Project Information

[Product Vision Document](https://docs.google.com/document/d/1PNvyYa1qH1uxq-YKAhYnAPhT5jSBBE3XgYDzgQpFIUE/edit#heading=h.p0mtiic9v46n)

[Med Cabinet Project Pitch and Rubrics](https://www.notion.so/Med-Cabinet-7960b90bb485430483bb266f7b738308)


## Links:
*[MediCabinet](https://github.com/MediCabinet)

    *[Marketing](https://github.com/MediCabinet/marketing)

    *[ML-Engineering](https://github.com/MediCabinet/ml-engineering)

    *[Data-Engineering](https://github.com/MediCabinet/data-engineering)

    *[Front-End](https://github.com/MediCabinet/front-end)

    *[Back-End](https://github.com/MediCabinet/backend)
