__author__ = 'geoffc'
import cherrypy
import os

from api.resources.Todo import Todo
from api.resources.User import User
from api.resources.Project import Project

from api.tools.jsonify import jsonify

from api.services.user_service import UserService


class ResourceApi:
    todo = Todo()
    user = User()
    project = Project()



class Auth:
    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def login(self):
        user = cherrypy.request.json
        cookie = cherrypy.response.cookie
        username = user['name']

        service = UserService()
        if not service.does_username_exist(username):
            service.add_user(username)

        user = service.get_user_by_username(username)
        user['isLoggedIn'] = True

        cookie['user'] = user['_id']
        cookie['user']['path'] = '/'
        cookie['user']['max-age'] = 3600

        return user

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def logged_in(self):
        cookie = cherrypy.request.cookie
        service = UserService()


        if 'user' in cookie and service.gett_user(cookie['user'].value):

            user = service.get_user_by_id(cookie['user'].value)
            user['isLoggedIn'] = True
            return user
        else:
            return {
                'isLoggedIn': False
            }

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def logout(self):
        cherrypy.response.cookie['user'] = cherrypy.request.cookie['user'].value
        cherrypy.response.cookie['user']['path'] = '/'
        cherrypy.response.cookie['user']['expires'] = 0
        return {
            'isLoggedIn': False
        }


class App:
    pass


def _run():
    cherrypy.tools.jsonify = cherrypy.Tool('before_handler', jsonify, priority=30)

    cherrypy.tree.mount(App(), '/', config={
        '/': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': os.path.join(os.path.abspath(os.path.dirname(__file__)), 'ui'),
            'tools.staticdir.index': os.path.join(os.path.abspath(os.path.dirname(__file__)), 'ui', 'index.html'),
        },
    })

    cherrypy.tree.mount(Auth(), '/auth', config={})

    cherrypy.tree.mount(ResourceApi(), '/api/resources', config={
        '/': {},
        '/todo': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.jsonify.on': True
        },
        '/user': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.jsonify.on': True
        },
        '/project': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.jsonify.on': True
        }
    })

    cherrypy.config.update({
        'server.socket_host': "0.0.0.0",
        'server.socket_port': 8089,
        'server.thread_pool': 20,
        'engine.autoreload.on': True,
        'tools.sessions.on': True
    })
    cherrypy.engine.start()
    cherrypy.engine.block()

    return


"""
    cherrypy.tree.mount(Api(), '/api', config={
        '/': {},
        '/todo': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
        }
    })
"""

if __name__ == "__main__":
    _run()