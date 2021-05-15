import json
import boto3
import time
import datetime

REGION="<YOURREGIONGOESHERE>"

dynamodb = boto3.resource('dynamodb', region_name=REGION)
table = dynamodb.Table('PhotoGallery')

def lambda_handler(event, context):
    user_name = event['body-json']['username']
    title = event['body-json']['title']
    description = event['body-json']['description']
    tags = event['body-json']['tags']
    uploaded_file_url = event['body-json']['uploadedFileURL']
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

    photo_id=str(int(ts*1000))

    table.put_item(
        Item = {
            "PhotoId": photo_id,
            "Username": user_name,
            "CreationTime": timestamp,
            "Title": title,
            "Description": description,
            "Tags": tags,
            "URL": uploaded_file_url
        }
    )

    return {
        "statusCode": 200,
        "body": json.dumps(photo_id)
    }
     