# mongo.py

from flask import Flask
from flask import g
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from flask import make_response
from bson.objectid import ObjectId
from flask import current_app
import sys
import json

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'restdb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/crm1'

@app.errorhandler(404)
def not_found(error):
  return make_response(jsonify({'error':'Notfound' }),404)

#test with context
with app.app_context():
  mongo = PyMongo(app)
  star = mongo.db.accounts
  output = []
  for s in star.find():
    output.append({'id': str(s['_id']) ,'firstname' : s['firstname'], 'lastname' : s['lastname']})
  with current_app.test_request_context():
    ##print (jsonify({'result' : output}))
    print ( json.dumps(output) )


@app.before_request
def before_request():
  if request.mimetype == 'application/json':
   res = request.get_json()
  else:
   res = request.form
  g.request= res



@app.route('/accounts', methods=['GET'])
def get_all_stars():
  #star = mongo.db.accounts
  output = []
  for s in star.find():
    output.append({'id': str(s['_id']) ,'firstname' : s['firstname'], 'lastname' : s['lastname']})
  return jsonify({'result' : output})

@app.route('/star/<id>', methods=['GET'])
def get_one_star(id):
  star = mongo.db.accounts
  s = star.find_one({'_id' : ObjectId(id) })
  if s:
    output = {'id': str(s['_id']) ,'lastname' : s['lastname'], 'firstname' : s['firstname']}
  else:
    output = "No such name"
  return jsonify({'result' : output})

@app.route('/star', methods=['POST'])
def add_star():

  accounts = mongo.db.accounts


  #block moved to @app.before_request
  #if request.mimetype == 'application/json':
  # res = request.get_json()
  #else:
  # res = request.form

  res = g.request

  firstname = res['firstname']
  lastname = res['lastname']

  id = accounts.insert({'firstname': firstname, 'lastname': lastname})
  new = accounts.find_one({'_id': id })
  output = {'firstname' : new['firstname'], 'lastname' : new['lastname']}
  return jsonify({'ok' : 'ok'})
  #return jsonify(request.get_json(force=True))

if __name__ == '__main__':
    app.run(debug=True)

