import json
from django.forms.models import model_to_dict

def from_query_set(query_set):
    return list(query_set)

def from_model_object(object):
    print(object)
    return json.dumps(model_to_dict(object))
    