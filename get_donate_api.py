from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify

app = Flask(__name__)
api = Api(app)

db_connect = create_engine('sqlite:///locmnapthe.db')
conn = db_connect.connect()

class get_all_players(Resource):
    def get(self):
        query = conn.execute("select * from napthe") 
        return {'players': [i[0] for i in query.cursor.fetchall()]}

class get_by_name(Resource):
    def get(self, employee_id):
        query = conn.execute("select * from napthe where player =%d "  %int(employee_id))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class get_all(Resource):
    def get(self):
        query = conn.execute("select player, amount from player;")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

api.add_resource(get_all, '/api/napthe')
api.add_resource(get_by_name, '/api/napthe/id/<player>')
api.add_resource(get_all, '/api/napthe/all')
if __name__ == '__main__':
     app.run()
