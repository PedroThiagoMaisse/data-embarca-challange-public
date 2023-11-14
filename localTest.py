import handler
import traceback
import logging
import os
import sys
from dotenv import load_dotenv

load_dotenv()

def main():
    try:
        return True
        event = {}
        event['lambda_handler_1_result'] = {'responseBody': (handler.hello_1({"Payload": "input/inp_2023-09-20T14-29-57-ec.json"}, {''}))['body']}
        event['lambda_handler_2_result'] = {'responseBody': (handler.hello_2(event, {''}))['body']}
        print(event['lambda_handler_2_result']['responseBody']['outputLength'], 'Lines created\nAt:', os.environ['OUTPUT_FILE_PATH'])
        return True

    except Exception as e:
        logging.error(traceback.format_exc())
        return False

main()
