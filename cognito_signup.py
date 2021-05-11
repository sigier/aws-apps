import json 
import boto3
from botocore.exceptions import ClientError

REGION="<YOUR REGION GOES HERE>"
USER_POOL_ID="<YOUR USER POOL ID GOES HERE>"
CLIENT_ID="<YOUR CLIENT ID GOES HERE>"

cognito_client = boto3.client('cognito-idp', region_name=REGION)

def lambda_handler(event, context):
    username=event['body-json']['username']
    password=event['body-json']['password']
    name=event['body-json']['name']
    email=event['body-json']['email']
    result=False
    message=""
    response={}
    returndata={}
    userdata={}
    try:
        response = cognito_client.sign_up(
            ClientId=CLIENT_ID,
            Username=username,
            Password=password,
            UserAttribute=[
                {
                    'Name':'name',
                    'Value':name
                },
                {
                    'Name':'email',
                    'Value': email
                }
            ] 
        )
        result=True
        message="Signup is successfull"
    except ClientError as e:
        if e.response['Error']['Code']=='UsernameExistsException':
            return False
            message="User exists already!"
        if e.response['Error']['Code']=='ParamValidationError':
            return False
            message="Parameter Validation Error"
    userdata['username']=username
    userdata['name']=name
    userdata['email']=email
    userdata['result']=result
    userdata['message']=message
    userdata['userdata']=userdata

    return {
        "statusCode":200,
        "body":json.dumps(returndata)
    }


     