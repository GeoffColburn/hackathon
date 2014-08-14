__author__ = 'geoffc'
import cherrypy
from BaseResource import BaseResource
from bson.objectid import ObjectId
from ..services.user_service import UserService

@cherrypy.popargs('id')
class User(BaseResource):
    exposed = True

    def __init__(self):
        super(User, self).__init__()
        self.service = UserService()

    def GET(self, id=None):
        if id:
            item = self.service.get_user_by_id(id)
            cookie = cherrypy.request.cookie
            if 'user' in cookie:
                cookie_id = cookie['user'].value
                if cookie_id == id:
                    item['isLoggedIn'] = True

            return item
        else:
            items = self.service.get_users()
            return [i for i in items]



    @cherrypy.tools.json_in()
    def POST(self, id):
        item = cherrypy.request.json
        self.service.update_user(id, item)

    @cherrypy.tools.json_in()
    def DELETE(self, id):
        pass