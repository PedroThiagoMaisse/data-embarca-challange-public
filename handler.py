from services.getBucketObject import getBucketObject
from services.postBucketObject import postBucketData
from utils.dictToCsvString import dictToCsvString
from utils.jsonToDict import jsonToDict
from utils.plainify import plainifyDataList
from utils.filterKeys import filterKeys
import traceback
import logging
import os
import datetime

def getBucketJson(event, context):
    try:
        bucketData = getBucketObject(event['Payload'])
        baseJson = jsonToDict(bucketData)

        body = {
            "message": "The Get was executed successfully!",
            "output": baseJson['hits']
        }

        response = {
            "statusCode": 200,
            "body": body
        }

    except Exception as e:
        logging.error(traceback.format_exc())
        response = {
            "statusCode": 500,
            "body": e
        }

    return response


def treatData(event, context):
    try:
        plainifiedJson = plainifyDataList(event['lambda_handler_1_result']['responseBody']['output'])
        
        listWithAlteredKeys = filterKeys(plainifiedJson)

        body = {
            "message": "The manipulation was executed successfully!",
            "output": listWithAlteredKeys
        }

        response = {
            "statusCode": 200,
            "body": body
        }

    except Exception as e:
        logging.error(traceback.format_exc())
        response = {
            "statusCode": 500,
            "body": e
        }

    return response

def postDataAsCsv(event, context):
    try:
        previousData = event['lambda_handler_2_result']['responseBody']['output']
        generatedCSV = dictToCsvString(previousData)

        postBucketData(os.environ['OUTPUT_FILE_PATH'], generatedCSV)
        postBucketData('bin/' + datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y") + '.csv', generatedCSV)

        body = {
            "message": "The creation of the file was executed successfully!",
            "filePath": os.environ['BUCKET_NAME'] + '/' + os.environ['OUTPUT_FILE_PATH'] 
        }

        response = {
            "statusCode": 200,
            "body": body
        }

    except Exception as e:
        logging.error(traceback.format_exc())
        response = {
            "statusCode": 500,
            "body": e
        }

    return response