__author__ = 'Geoff'
import cherrypy
from BaseResource import BaseResource
from ..services.private_messaging import PrivateMessagingService


@cherrypy.popargs('id')
class PrivateMessage(BaseResource):
    exposed = True

    def __init__(self):
        super(PrivateMessage, self).__init__()
        self.service = PrivateMessagingService()

    def GET(self, id=None, user_id=None, unread=None):

        if id:
            item = self.service.get_private_message(id)
            return item

        if user_id:
            items = self.service.get_private_messages_for_user(user_id)
            return [i for i in items]

        if unread:
            user_id = self.get_executing_user_id()
            n = self.service.get_unread_count_for_user(user_id)
            return {'unread': n}

        user_id = self.get_executing_user_id()
        items = self.service.get_private_messages_for_user(user_id)
        return [i for i in items]

    @cherrypy.tools.json_in()
    def POST(self, id=None, unread=True):
        item = cherrypy.request.json
        from_user_id = self.get_executing_user_id()
        to_user_id = item['to_user_id']
        self.service.add_private_message(from_user_id, to_user_id, item['title'], item['text'])

        if not unread and id:
            self.service.set_private_message_unread_status(id, False)

    @cherrypy.tools.json_in()
    def DELETE(self, id):
        pass