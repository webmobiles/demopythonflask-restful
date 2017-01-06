from flask import Flask
from dbMongo import mongoConfig
from flask import request
from flask import make_response
from flask import jsonify
from flask import g
from flask_pymongo import PyMongo

db = PyMongo()

def create_app():

    app = Flask(__name__)

    @app.errorhandler(404)
    def not_found(error):
      return make_response(jsonify({'error':'Notfound' }),404)


    @app.before_request
    def before_request():
      if request.mimetype == 'application/json':
       res = request.get_json()
      else:
       res = request.form
      g.request= res

    app.config.from_object(mongoConfig)
    mongoConfig.init_app(app)

    db.init_app(app)


    from routes.accounts import accountRoute

    app.register_blueprint(accountRoute, url_prefix='/accounts')

    return app
