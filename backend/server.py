#coding: utf8

'''
Démarrage de l'application
'''


import flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

app_globals = {}


def get_app():
    if app_globals.get('app', False):
        return app_globals['app']
    app = flask.Flask(__name__)
    app.config.from_pyfile('./config.py')
    db.init_app(app)


    from pypnnomenclature.routes import routes
    app.register_blueprint(routes, url_prefix='/nomenclatures')

    from modules.users.routes import routes
    app.register_blueprint(routes, url_prefix='/users')

    from modules.pr_contact.routes import routes
    app.register_blueprint(routes, url_prefix='/pr_contact')


    app_globals['app'] = app
    return app

app = get_app()
CORS(app)

if __name__ == '__main__':
    from flask_script import Manager
    Manager(app).run()