import json
from services.getBucketObject import getBucketObject
from services.postBucketObject import postBucketData
from utils.dictToCsvString import dictToCsvString
from utils.jsonToDict import jsonToDict
from utils.plainify import plainifyData
from utils.filterKeys import filterKeys
import subprocess
import traceback
import logging
import os

def hello_1(event, context):
    try:
        bucketData = getBucketObject(event['Payload'])
        baseJson = jsonToDict(bucketData)
        plainifiedJson = plainifyData(baseJson['hits'])
        
        listWithAlteredKeys = filterKeys(plainifiedJson)

        body = {
            "message": "The Get and manipulation of information was executed successfully!",
            "input": event,
            "outputLength": len(listWithAlteredKeys),
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


def hello_2(event, context):
    try:
        previousData = event['lambda_handler_1_result']['responseBody']
        generatedCSV = dictToCsvString(previousData['output'])

        r = postBucketData(os.environ['OUTPUT_FILE_PATH'], generatedCSV)

        body = {
            "message": "The creation of the file was executed successfully!",
            "outputLength": previousData['outputLength']
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
