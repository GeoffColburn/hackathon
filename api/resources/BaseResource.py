__author__ = 'Geoff'
import cherrypy
from pymongo import MongoClient


class BaseResource(object):
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client["hack"]

    def get_executing_user_id(self):
        cookie = cherrypy.request.cookie
        if 'user' in cookie:
            return cookie['user'].value
        else:
            None

