import boto3
import json

AWS_KEY="<YOURAWSKEYGOESHERE>"
AWS_SECRET="<YOURAWSSECRETGOESHERE>"
AWS_REGION="<YOURAWSREGIONGOESHERE>"
BUCKET="<YOURBUCKETGOESHERE>"
FILENAME="<YOURFILENAMEGOESHERE>"
SNIPPET="<YOURFILECONTENTGOESHERE>"

s3 = boto3.client('s3', aws_access_key_id=AWS_KEY, aws_secret_access_key=AWS_SECRET)

s3.put_object(Bucket=BUCKET, Key=FILENAME, Body=SNIPPET)