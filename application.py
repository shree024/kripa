from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS, cross_origin
import login_signup
# import  connect_table

# importing necessary packages

application = Flask(__name__)
CORS(application)
api = Api(application)
CORS(application, support_credentials=True)

# cog = connect_table.cogclient

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
        # login_signup.login(args['username'], args['password'])
        if result != False:
            jsonData = jsonify(result)
            return jsonData
        else:
            return {"success": "false"}


# SNSReg section
@application.route('/api/v1/snsreg', methods=['POST', 'GET', 'OPTIONS'])
@cross_origin(supports_credentials=True)
def post_snsreg():
    if (request.method == 'POST'):
        args = request.get_json()
        result = login_signup.mobreg(args['mob'])
        print(result)
        if result != False:
            jsonData = jsonify(result)
            return jsonData
        else:
            return {"success": "false"}

# SNSVerify section
@application.route('/api/v1/snsver', methods=['POST', 'GET', 'OPTIONS'])
@cross_origin(supports_credentials=True)
def post_snsver():
    if (request.method == 'POST'):
        args = request.get_json()
        result = login_signup.mobver(args['mob'],args['code'])
        print(result)
        if result != False:
            result1 = login_signup.msgsub(args['mob'])
            jsonData = jsonify(result1)
            return jsonData
        else:
            return {"success": "false"}

# SNSVerify section
@application.route('/api/v1/snspub', methods=['POST', 'GET', 'OPTIONS'])
@cross_origin(supports_credentials=True)
def post_snsmsg():
    if (request.method == 'POST'):
        args = request.get_json()
        result = login_signup.msgpub(args['msg'])
        print(result)
        if result != False:
            jsonData = jsonify(result)
            return jsonData
        else:
            return {"success": "false"}




@application.route('/')
def hello_world():  # put applicationl's code here
    # username = "abcd.xyz@gmail.com"
    # password = "#Abc1234"
    
    # COGNITO_USER_CLIENT_ID = "722d9o00ns6alnb92n37g1imh5"
    # cog.sign_up(
    # ClientId=COGNITO_USER_CLIENT_ID,
    # Username=username,
    # Password=password,
    # UserAttributes=[{"Name": "name", "Value": "shree"},{"Name":"phone_number","Value":"+1234567890"}],
    # )
    return 'Hello user'


if __name__ == '__main__':
    application.run(debug=True)
