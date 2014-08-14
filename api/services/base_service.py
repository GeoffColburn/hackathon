from pymongo import MongoClient
from bson.objectid import ObjectId


class BaseService(object):
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client["hack"]