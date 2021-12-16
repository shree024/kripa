import json

from flask_restful import Api, Resource, reqparse
import  connect_table
from awscli.errorhandler import ClientError


table= connect_table.table1
cog = connect_table.cogclient
snsmsg = connect_table.snsclient


COGNITO_USER_CLIENT_ID = "23rvodick24unj9av85of3p4vl"

# Login Block
def login(usr, pwd):
    try:

        response = cog.initiate_auth(
        ClientId=COGNITO_USER_CLIENT_ID,
        AuthFlow="USER_PASSWORD_AUTH",
        AuthParameters={"USERNAME": usr, "PASSWORD": pwd},
        )
        accTo = response["AuthenticationResult"]["AccessToken"]
        response = cog.get_user(AccessToken=accTo)
        
        res = json.loads(json.dumps(response))

        for i in range(0,len(res['UserAttributes'])):
            if(res['UserAttributes'][i]['Name']=="name") :
                nam = res['UserAttributes'][i]['Value']

        key={
            "username": usr,
            "name": nam
        }       
        upd={
            "token": {'Value' : accTo}
        }

        table.update_item(Key=key, AttributeUpdates=upd)

        return json.loads(json.dumps(response))
    except ClientError as e:
        print(e.response['Error']['Message'])
        return {"success": "false"}



def signUp(usr,pwd,name,mob):
    try:
        
        cog.sign_up(
            ClientId=COGNITO_USER_CLIENT_ID,
            Username=usr,
            Password=pwd,
            UserAttributes=[{"Name": "name", "Value": name},{"Name":"custom:ph_number","Value":mob}],
        )

        return {"success": "true"}
    except ClientError as e:
        print(e.response['Error']['Message'])
        return {"success": "false"}


def mobreg(mob):
    try:
        snsmsg.create_sms_sandbox_phone_number(
        PhoneNumber=mob,
        LanguageCode='en-US'
        )
        return {"success": "true"}
    except ClientError as e:
        print(e.response['Error']['Message'])
        return {"success": "false"}

def mobver(mob,code):
    try:
        snsmsg.verify_sms_sandbox_phone_number(
        PhoneNumber=mob,
        OneTimePassword=code
        )
        return {"success": "true"}
    except ClientError as e:
        print(e.response['Error']['Message'])
        return {"success": "false"}

def msgpub(mob,msg):
    try:
        snsmsg.publish(PhoneNumber=mob, Message=msg)
        return {"success": "true"}
    except ClientError as e:
        print(e.response['Error']['Message'])
        return {"success": "false"}
    
