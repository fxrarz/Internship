"""
RESTFUL API USING FLASK AND POSTMAN

Requirement: Flask, Google Chrome, Postman

Written on: 26 April 2022

Tested on: Linux(debian)

Author: A.S. Faraz Ahmed

Description:

    Sample input: {"param1" : "value1", "param2": "value2"}
    url: http://127.0.0.1:5000/jsonapi
    
"""
from flask import Flask, request, render_template, make_response
from flask_restful import Api, Resource
import json
import re

app = Flask(__name__)
api = Api(app)

class apis(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('index.html'),200,headers)
        
    def post(self):
        todo_id = str(request.get_json(force=True, silent=True, cache=False))
        todo_id = re.sub("'", '"', todo_id)
        print(todo_id)
        if len(json.loads(todo_id).keys()) >= 2:
            return 'success', 201
        return '', 400
        
api.add_resource(apis, '/jsonapi')

if __name__ == '__main__':
    app.run(debug=True)
