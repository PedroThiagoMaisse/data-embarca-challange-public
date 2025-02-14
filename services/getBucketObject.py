import os 
import boto3
import traceback
import logging

def getBucketObject(archive):
    try:
        s3_client = boto3.client('s3', 
        aws_access_key_id= os.environ['ACCESS_KEY_ID'], 
        aws_secret_access_key=os.environ['SECRET_ACCESS_KEY']
        )

        response = s3_client.get_object(Bucket=os.environ['BUCKET_NAME'], Key=archive)

        return response['Body'].read().decode('utf-8')
    except Exception as e:
        logging.error(traceback.format_exc())