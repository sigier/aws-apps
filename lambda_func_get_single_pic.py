import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

REGION="<YOURREGIONGOESHERE>"

dynamodb = boto3.resource('dynamodb', region=REGION)
table = dynamodb.Table('PhotoGallery')

def lambda_handler(event, context):
    photoId=event['pathParameters']['id']
    response=table.scan(
        FilterExpression=Attr('PhotoId').eq(photoId)
        )
        
    items=response['Items']
    return {
        "statusCode": 200,
        "body": json.dumps(items)    
    } 
