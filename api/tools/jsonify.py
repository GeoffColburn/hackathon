__author__ = 'Geoff'
import json
import bson
import cherrypy


def encode(obj):
    if isinstance(obj, bson.objectid.ObjectId):
        return str(obj)
    return json.dumps(obj)


def handler(*args, **kwargs):
    request = cherrypy.serving.request
    value = request._json_inner_handler(*args, **kwargs)
    return json.dumps(value, default=encode, sort_keys=True)


def jsonify():
    request = cherrypy.serving.request
    request._json_inner_handler = request.handler
    request.handler = handler

    cherrypy.serving.response.headers['Content-Type'] = 'application/json'
