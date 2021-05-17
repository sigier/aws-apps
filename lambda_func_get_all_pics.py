import json
import boto3 

REGION="<YOURREGIONGOESHERE>"

dynamodb = boto3.resource('dynamodb', region=REGION)
table = dynamodb.Table('PhotoGallery')

def lambda_handler(event, context):
    response = table.scan()
    items = response['Items']
    
    return {
        "statusCode": 200,
        "body": json.dumps(items)
    }