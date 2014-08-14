__author__ = 'geoffc'
from base_service import BaseService
from bson.objectid import ObjectId


class PrivateMessagingService(BaseService):
    def __init__(self):
        super(PrivateMessagingService, self).__init__()
        self.collection = self.db.private_messages

    def add_private_message(self, from_user_id, to_user_id, title, message):
        self.collection.insert({
            'from_user_id': from_user_id,
            'to_user_id': to_user_id,
            'title': title,
            'message': message,
            'unread': True
        })

    def get_private_message(self, id):
        item = self.collection.find_one({'_id': ObjectId(id)})
        return item

    def get_private_messages_for_user(self, user_id):
        items = self.collection.find({'to_user_id': user_id, 'unread': True})
        return items

    def set_private_message_unread_status(self, id, unread):
        item = self.collection.update({'_id': ObjectId(id)}, {'$set': {'unread': unread}})
        return item

    def get_unread_count_for_user(self, user_id):
        items = self.collection.find({'to_user_id': user_id, 'unread': True})
        n = items.count()
        return n

