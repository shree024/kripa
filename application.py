from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS, cross_origin
import login_signup

application = Flask(__name__)
CORS(application)
api = Api(application)
CORS(application, support_credentials=True)



# SignUP section
@application.route('/api/v1/new_data', methods=['POST', 'GET', 'OPTIONS'])
@cross_origin(supports_credentials=True)
def post():
    if (request.method == 'POST'):
        args = request.get_json()
        result = login_signup.signUp(args['username'], args['password'], args['name'], args['mob'])
        print(result)
        if result != False:
            jsonData = jsonify(result)
            return jsonData
        else:
            return {"success": "false"}

# Login section
@application.route('/api/v1/check', methods=['POST', 'GET', 'OPTIONS'])
@cross_origin(supports_credentials=True)
def post_login():
    if (request.method == 'POST'):
        print("test0")
        args = request.get_json()
        result = login_signup.login(args['username'], args['password'])
        print("test")
        print(result)
        if result != False:
            jsonData = jsonify(result)
            return jsonData
        else:
            return {"success": "false"}


@application.route('/')
def hello_world():  
    return 'Hello user'


if __name__ == '__main__':
    application.run(debug=True)
