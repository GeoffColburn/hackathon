__author__ = 'geoffc'
from pymongo import MongoClient
from bson.objectid import ObjectId


class UserService(object):
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client["hack"]
        self.collection = self.db.users
        self.default_avatar = '/images/anon.jpg'

    def add_user(self, username):
        self.collection.insert({'username': username})

    def does_username_exist(self, username):
        user = self.collection.find_one({'username': username})
        return user != None

    def get_user_by_id(self, id):
        user = self.collection.find_one({'_id': ObjectId(id)})
        if not user:
            return None

        user['avatarUrl'] = user['avatarUrl'] if 'avatarUrl' in user else self.default_avatar
        user['_id'] = str(user['_id'])

        return user

    def get_user_by_username(self, username):
        user = self.collection.find_one({'username': username})
        if not user:
            return None

        user['avatarUrl'] = user['avatarUrl'] if 'avatarUrl' in user else self.default_avatar
        user['_id'] = str(user['_id'])

        return user

    def update_user(self, id, user):
        user['_id'] = ObjectId(id)
        self.collection.update({'_id': ObjectId(id)}, user, True)

    def get_users(self):
        items = self.collection.find()
        return items
