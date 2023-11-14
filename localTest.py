import handler
import traceback
import logging
import os
import sys
from dotenv import load_dotenv

load_dotenv()

def main():
    try:
        event = {}
        event['lambda_handler_1_result'] = {'responseBody': (handler.getBucketJson({"Payload": "input/inp_2023-09-20T14-29-57-ec.json"}, {''}))['body']}
        print(event['lambda_handler_1_result']['responseBody']['message'])
        event['lambda_handler_2_result'] = {'responseBody': (handler.treatData(event, {''}))['body']}
        print(event['lambda_handler_2_result']['responseBody']['message'])
        event['lambda_handler_3_result'] = {'responseBody': (handler.postDataAsCsv(event, {''}))['body']}
        print(event['lambda_handler_3_result']['responseBody']['message'])

        return True

    except Exception as e:
        logging.error(traceback.format_exc())
        sys.exit(1)

main()
