from bson.objectid import ObjectId
from base_service import BaseService


class ProjectService(BaseService):
    def __init__(self):
        super(ProjectService, self).__init__()
        self.collection = self.db.projects

    def add_project(self, owner_id, project):
        project['owner_id'] = owner_id
        if '_id' in project:
            project['_id'] = ObjectId(project['_id'])
            self.collection.update({'_id': project['_id']}, project, True)
        else:
            self.collection.insert(project)

    def get_projects_by_user_id(self, user_id):
        items = self.collection.find({'owner_id': user_id})
        return items

    def get_project_by_id(self, id):
        item = self.collection.find_one({'_id': ObjectId(id)})
        return item

    def get_projects(self):
        items = self.collection.find()
        return items

    def get_projects_by_tags(self, tags):
        query = dict((k, True) for k in tags)
        items = self.collection.find({'skills': query})
        return items