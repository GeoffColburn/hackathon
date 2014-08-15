__author__ = 'Geoff'
import cherrypy
from BaseResource import BaseResource
from ..services.project_service import ProjectService


@cherrypy.popargs('id')
class Project(BaseResource):
    exposed = True

    def __init__(self):
        super(Project, self).__init__()
        self.service = ProjectService()

    def GET(self, id=None, user_id=None, tags=None):
        if user_id:
            items = self.service.get_projects_by_user_id(user_id)
            if items:
                return [i for i in items]

        if id:
            item = self.service.get_project_by_id(id)
            item['isEditable'] = item['owner_id'] == self.get_executing_user_id()
            return item

        if tags:
            tag_list = tags.split(',')
            items = self.service.get_projects_by_tags(tag_list)
            return [i for i in items]

        items = self.service.get_projects()
        return [i for i in items]

    @cherrypy.tools.json_in()
    def POST(self, id=None):
        item = cherrypy.request.json
        owner_id = self.get_executing_user_id()
        self.service.add_project(owner_id, item)

    @cherrypy.tools.json_in()
    def DELETE(self, id):
        pass