from flask import Blueprint
from flask import jsonify
from bson.objectid import ObjectId
from flask import g
from application import db as dbmongo

accountRoute = Blueprint('accountRoute', __name__)


#with current.app_context():
#with app.test_request_context():
hh='hola'
@accountRoute.route('/', methods=['GET'])
def get_all():
  accountDb = dbmongo.db.accounts
  print (hh)
  output = []
  for s in accountDb.find():
    output.append({'id': str(s['_id']) ,'firstname' : s['firstname'], 'lastname' : s['lastname']})
  return jsonify({'result' : output})

@accountRoute.route('/<id>', methods=['GET'])
def get_one(id):
  accountDb = dbmongo.db.accounts
  s = accountDb.find_one({'_id' : ObjectId(id) })
  if s:
    output = {'id': str(s['_id']) ,'lastname' : s['lastname'], 'firstname' : s['firstname']}
  else:
    output = "No such name"
  return jsonify({'result' : output})

@accountRoute.route('/', methods=['POST'])
def add():

  accountDb = dbmongo.db.accounts
  res = g.request

  firstname = res['firstname']
  lastname = res['lastname']

  id = accountDb.insert({'firstname': firstname, 'lastname': lastname})
  new = accountDb.find_one({'_id': id })
  output = {'firstname' : new['firstname'], 'lastname' : new['lastname']}
  return jsonify({'ok' : 'ok'})
