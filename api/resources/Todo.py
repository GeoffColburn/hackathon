__author__ = 'Geoff'
import cherrypy
from BaseResource import BaseResource
from bson.objectid import ObjectId


@cherrypy.popargs('id')
class Todo(BaseResource):
    exposed = True

    def __init__(self):
        super(Todo, self).__init__()
        self.collection = self.db.todos

    def GET(self, id=None):
        if id:
            item = self.collection.find_one({'_id': ObjectId(id)})
            return item
        else:
            items = [i for i in self.collection.find()]
            return items

    @cherrypy.tools.json_in()
    def POST(self):
        item = cherrypy.request.json
        self.collection.insert(item)

    @cherrypy.tools.json_in()
    def DELETE(self, id):
        self.collection.remove({'_id': ObjectId(id)})
