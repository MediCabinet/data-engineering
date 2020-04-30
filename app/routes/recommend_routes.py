# import packages
import pickle
from sklearn.neighbors import NearestNeighbors
import numpy
import json
import pandas as pd
from flask import Blueprint, jsonify, render_template, request

from app.models import db, Base, Strain, parse_records

recommend_routes = Blueprint("recommend_routes", __name__)

# open pickle with trained model
with open('./app/data/model_pickle', 'rb') as f:
    pickle = pickle.load(f)

# nearest neighbor mopdel
nn = NearestNeighbors(metric='cosine', algorithm='brute',
                      n_neighbors=20, n_jobs=-1)

nn.fit(pickle)

negative_list = ['anxious', 'dizzy', 'dry eyes',
                 'dry mouth', 'headache', 'paranoid']
effect_list = ['creative', 'energetic', 'euphoric',
               'focused', 'happy', 'hungry', 'relaxed', 'sleepy']
ailment_list = ['anxiety', 'depression', 'fatigue',
                'headaches', 'lack of appetite', 'pain', 'stress']

columns = ['anxious', 'dizzy', 'dry eyes', 'dry mouth', 'headache', 'paranoid', 'creative', 'energetic',
           'euphoric', 'focused', 'happy', 'hungry', 'relaxed', 'sleepy', 'anxiety', 'depression', 'fatigue',
           'headaches', 'lack of appetite', 'pain', 'stress']

@recommend_routes.route("/strain/qa_form")
def strain_model_form():
    return render_template("qa_form.html")

@recommend_routes.route("/strain/recommend", methods=["POST"])
def recommend(n: int = 10):

    effect_dict = rq.form.getlist("effect_list")
    negative_dict = rq.form.getlist("negative_list")
    ailments_dict = rq.form.getlist("ailment_list")
	
    dict_of_inputs = {"effects": effect_dict, 
                      "negatives": negative_dict,
                      "ailments": ailments_dict
                }
    
    dict_of_inputs_json = jsonify(dict_of_inputs)
    
    return dict_of_inputs_json

    desired_dict = json.loads(request)
    effects, negatives, ailments = {
        desired_dict.get("effects"),
        desired_dict.get("negatives"),
        desired_dict.get("ailments")
    }
    
    effects = [effect.lower() for effect in effects]
    negatives = [negative.lower() for negative in negatives]
    ailments = [ailment.lower() for ailment in ailments]

    for index, effect in enumerate(effects):
        if effect in columns:
            effects[index] = columns.index(effect)

    for index, negative in enumerate(negatives):
        if negative in columns:
            negatives[index] = columns.index(negative)

    for index, ailment in enumerate(ailments):
        if ailment in columns:
            ailments[index] = columns.index(ailment)

    vector = [
        0 for _ in range(len(columns))
    ]

    weight = 100

    for index in effects:
        if isinstance(index, int):
            vector[index] = weight
            weight *= .8
            weight = int(weight)

    weight = 100

    for index in negatives:
        if isinstance(index, int):
            vector[index] = weight
            weight *= .8
            weight = int(weight)

    weight = 100

    for index in ailments:
        if isinstance(index, int):
            vector[index] = weight
            weight *= .8
            weight = int(weight)

    data = numpy.array(vector)
    request_series = pd.Series(data, index=columns)
    distance, neighbors = nn.kneighbors([request_series])

    list_strains = []
    for points in neighbors:
        for index in points:
            list_strains.append(index)

    return list_strains[:n]


# # import packages
# import pickle
# from sklearn.neighbors import NearestNeighbors
# import numpy
# import json
# import pandas as pd
# from flask import Blueprint, jsonify, render_template, request

# from app.models import db, Base, Strain, parse_records

# recommend_routes = Blueprint("recommend_routes", __name__)

# # open pickle with trained model
# with open('./app/data/model_pickle', 'rb') as f:
#     pickle = pickle.load(f)

# # nearest neighbor mopdel
# nn = NearestNeighbors(metric='cosine', algorithm='brute',
#                       n_neighbors=20, n_jobs=-1)

# nn.fit(pickle)

# negative_list = ['anxious', 'dizzy', 'dry eyes',
#                  'dry mouth', 'headache', 'paranoid']
# effect_list = ['creative', 'energetic', 'euphoric',
#                'focused', 'happy', 'hungry', 'relaxed', 'sleepy']
# ailment_list = ['anxiety', 'depression', 'fatigue',
#                 'headaches', 'lack of appetite', 'pain', 'stress']

# columns = ['anxious', 'dizzy', 'dry eyes', 'dry mouth', 'headache', 'paranoid', 'creative', 'energetic',
#            'euphoric', 'focused', 'happy', 'hungry', 'relaxed', 'sleepy', 'anxiety', 'depression', 'fatigue',
#            'headaches', 'lack of appetite', 'pain', 'stress']

# @recommend_routes.route("/strain/qa_form")
# def strain_model_form():
#     return render_template("qa_form.html")

# @recommend_routes.route("/strain/recommend", methods=["POST"])
# def recommend(request: dict, n: int = 10):
#     desired_dict = json.loads(request)
#     effects, negatives, ailments = (
#         desired_dict.get("effects"),
#         desired_dict.get("negatives"),
#         desired_dict.get("ailments")
#     )
#     effects = [effect.lower() for effect in effects]
#     negatives = [negative.lower() for negative in negatives]
#     ailments = [ailment.lower() for ailment in ailments]

#     for index, effect in enumerate(effects):
#         if effect in columns:
#             effects[index] = columns.index(effect)

#     for index, negative in enumerate(negatives):
#         if negative in columns:
#             negatives[index] = columns.index(negative)

#     for index, ailment in enumerate(ailments):
#         if ailment in columns:
#             ailments[index] = columns.index(ailment)

#     vector = [
#         0 for _ in range(len(columns))
#     ]

#     weight = 100

#     for index in effects:
#         if isinstance(index, int):
#             vector[index] = weight
#             weight *= .8
#             weight = int(weight)

#     weight = 100

#     for index in negatives:
#         if isinstance(index, int):
#             vector[index] = weight
#             weight *= .8
#             weight = int(weight)

#     weight = 100

#     for index in ailments:
#         if isinstance(index, int):
#             vector[index] = weight
#             weight *= .8
#             weight = int(weight)

#     data = numpy.array(vector)
#     request_series = pd.Series(data, index=columns)
#     distance, neighbors = nn.kneighbors([request_series])

#     list_strains = []
#     for points in neighbors:
#         for index in points:
#             list_strains.append(index)

#     return list_strains[:n]