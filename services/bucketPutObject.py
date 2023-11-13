import os 
import boto3
from dotenv import load_dotenv

load_dotenv()

def postBucketData(fileName, data):
    s3_client = boto3.client('s3', 
    aws_access_key_id= os.environ['AWS_ACCESS_KEY_ID'], 
    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY']
    )

    response = s3_client.put_object(Bucket=os.environ['BUCKET_NAME'], Key=fileName, Body=data)
    
    # Check if the upload was successful
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        return {'success': True, 'data': response}
    else:
        return {'success': False, 'data': response} 