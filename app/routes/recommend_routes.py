# import packages
import pickle
from sklearn.neighbors import NearestNeighbors
import numpy
import json
import pandas as pd
from flask import Blueprint, jsonify, request, render_template

from app.models import Cabinet, db, parse_records

recommend_routes = Blueprint("recommend_routes", __name__)

# open pickle with trained model
with open('./data/model_pickle', 'rb') as f:
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

columns = [
    'anxious',
    'dizzy',
    'dry eyes',
    'dry mouth',
    'headache',
    'paranoid',
    'creative',
    'energetic',
    'euphoric',
    'focused',
    'happy',
    'hungry',
    'relaxed',
    'sleepy',
    'anxiety',
    'depression',
    'fatigue',
    'headaches',
    'lack of appetite',
    'pain',
    'stress']


@recommend_routes.route("/cabinet")
def cabinet():
    db_cabinet = Cabinet.query.all()
    cabinet_response = parse_records(db_cabinet)
    return jsonify(cabinet_response)


@recommend_routes.route("/recommend", methods=['GET', 'POST'])
def recommender():
    """
    creates list with top n recommended strains.

    Paramaters
    __________

    request: dictionary (json object)
        list of user's desired effects listed in order of user ranking.
        {
            "effects":[],
            "negatives":[],
            "ailments":[]
        }
    n: int, optional
        number of recommendations to return, default 10.

    Returns
    _______

    list_strains: python list of n recommended strains.
    """
    desired_dict = request.json
    n = 10
    effects, negatives, ailments = (
        desired_dict.get("effects"),
        desired_dict.get("negatives"),
        desired_dict.get("ailments")
    )
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

    return_list = [
        str(val)
        for val in list_strains[:n]
    ]
    
    records = parse_records(Cabinet.query.filter(Cabinet.model_id.in_(return_list)).all())
    
    return jsonify(records)
   

   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    """
    desired_dict = request.json
    n=5
    effects, negatives, ailments = (
        desired_dict.get("effects"),
        desired_dict.get("negatives"),
        desired_dict.get("ailments")
    )
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

recommended = strains_df.iloc[list_strains].head(n)
result = {
    "model_id": recommended.to_dict("records")
}

return result


    return_list = [
            int(val)
            for val in list_strains
        ]
    records = []
    # for val in return_list[:n]:
    records.append(parse_records(Cabinet.query.filter(Cabinet.model_id.in_(return_list)).all()))
    output = []
    if sum([len(rl) for rl in records]) > 0:
        for rl in records:
            if len(rl) > 0:
                print(len(rl))
                output.append([r for r in rl])
        return jsonify(output)
    else:
        return jsonify("NULL")

    
    # return jsonify(records)
    
    
        def get_strain(ids, size):
        # Create an empty dictionary to return
        results = {}

        # Loop through all IDs recieved from the predict function in search()
        for x,index in zip(ids, range(0,size)):
            # Create a base result with {"id":"x"} where x is the current strain index
            sub_result = {"id":str(x)}
            # Query the database for the strain index and add it to the dict
            sub_result['data'] = Strain.query.filter(Strain.index==int(x)).first().__repr__()
            # Add the sub_result to the main results dictionary
            results['{}'.format(index)] = sub_result

        # Return the results in a dictionary
        return results


    
    records = parse_records(Cabinet.query.filter(Cabinet.model_id == (2,3)))

    

    for val in return_list[:n]:
        records.append(parse_records(Cabinet.query.filter(Cabinet.model_id == [val]).all()))

    

    output = []
    if sum([len(rl) for rl in records]) > 0:
        for rl in records:
            if len(rl) > 0:
                print(len(rl))
                output.append([r for r in rl])
        return jsonify(output)
    else:
        return jsonify("NULL")
    # Solution provided by Alex & Trent data solutions inc. 


    return jsonify(records)


    recommended_list = [intersection_list, intersection_list2, intersection_list3]
    print("recommended_list", recommended_list, "\n\n")

    #if len(intersection_list) + len(intersection_list2) + len(intersection_list3) == 3:
    #    for record_list in recommended_list:
    #        for i in range(len(record_list)):
    #                return jsonify(record_list[i])

    #for rl in recommended_list:
    #    print(rl)
    
    results_strains_list = []
    if sum([len(rl) for rl in recommended_list]) > 0:
    #if len(intersection_list) + len(intersection_list2) + len(intersection_list3) > 0:
        for rl in recommended_list:
            if len(rl) > 0:
                print(len(rl))
                results_strains_list.append([r for r in rl])
                #for i in range(len(rl)):
        return jsonify(str(results_strains_list))
    else:
        return jsonify("According to Alex this means the code is FUBAR")






    # return jsonify(return_list)


        # Create an empty dictionary to return
        results = {}

        # Loop through all IDs recieved from the predict function in search()
        for x,index in zip(ids, range(0,size)):
            # Create a base result with {"id":"x"} where x is the current strain index
            sub_result = {"id":str(x)}
            # Query the database for the strain index and add it to the dict
            sub_result['data'] = Strain.query.filter(Strain.index==int(x)).first().__repr__()
            # Add the sub_result to the main results dictionary
            results['{}'.format(index)] = sub_result

        # Return the results in a dictionary
    
    
    data = numpy.array(vector)
    request_series = pd.Series(data, index=columns)
    distance, neighbors = nn.kneighbors([request_series])

    list_strains = []
    for points in neighbors:
        for index in points:
            list_strains.append(index)

    return_list = [
        int(val)
        for val in list_strains
    ]

    records = []
    
    for val in return_list[:n]:
        records.append(parse_records(Cabinet.query.filter(Cabinet.model_id == val).all()))

    if sum([len(rl)])

    return jsonify(records)
    """