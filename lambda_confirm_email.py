import json
import boto3
from botocore.exceptions import ClientError

REGION="<YOURREGIONGOESHERE>"
USER_POOL_ID="<YOURUSERPOOLIDGOESHERE>"
CLIENT_ID="<YOURUSERIDGOESHERE>"

cognito_client = boto3.client('cognito-idp', region_name=REGION)

def lambda_handler(event, context):
    user_name=event['body-json']['username']
    code=event['body-json']['code']
    result=False
    message=""
    response={}
    return_data={}
    try:
        response = cognito_client.confirm_sign_up(
            ClientId=CLIENT_ID,
            Username=user_name,
            ConfirmationCode=code
        )
    except ClientError as e:
        message="Error in confirming email"
        if e.response['Error']['Code']=='UserNotFoundException':
            result=False
            message="User not found by email"
        if e.response['Error']['Code']=='CodeMismatchException':
            result=False
            message="User code string mismatch"
        if e.response['Error']['Code']=='ParamValidationException':
            result=False
            message="Parameter Validation Exception"
        if e.response['Error']['Code']=='ExpiredCodeExeption':
            result=False
            message="Provided code string is expired"
        if e.response['Error']['Code']=='NotAuthorizedException':
            result=False
            message="User confirmed already"
    return_data['result']=result
    return_data['message']=message

    return {
        "statusCode": 200,
        "body": json.dumps(return_data)

    }
    
