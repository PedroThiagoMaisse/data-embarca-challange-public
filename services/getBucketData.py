import os 
import boto3
from dotenv import load_dotenv

load_dotenv()

def getBucketData(archive):
    s3_client = boto3.client('s3', 
    aws_access_key_id= os.environ['AWS_ACCESS_KEY_ID'], 
    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY']
    )

    response = s3_client.get_object(Bucket=os.environ['BUCKET_NAME'], Key=archive)

    return response['Body'].read().decode('utf-8')