import os 
import boto3
import traceback
import logging

def postBucketData(fileName, data):
    try:
        s3_client = boto3.client('s3', 
        aws_access_key_id= os.environ['ACCESS_KEY_ID'], 
        aws_secret_access_key=os.environ['SECRET_ACCESS_KEY']
        )

        response = s3_client.put_object(Bucket=os.environ['BUCKET_NAME'], Key=fileName, Body=data)
        
        # Check if the upload was successful
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return {'success': True, 'data': response}
        else:
            return {'success': False, 'data': response}

    except Exception as e:
        logging.error(traceback.format_exc())