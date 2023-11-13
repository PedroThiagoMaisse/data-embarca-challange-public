from utils.jsonToDict import jsonToDict 
from utils.plainify import plainifyData
from utils.filterKeys import filterKeys
import utils.dictToCsvString as dictToCsvString


jsonEx = """[{
            "_index": "data-production-2023-09-20",
            "_id": "ZVGls4oBNkLSxFfA3kR4",
            "_score": 2.8663144,
            "_source": {
                "name": "Seats",
                "type": "Integration",
                "app_name": "sales-web",
                "session_id": "109910961642a185cb16873e388e2486",
                "payload": {
                    "request": {
                        "origin_id": "14760",
                        "destination_id": "584",
                        "date": "2023-11-01",
                        "operator_id": null,
                        "white_label_request": false,
                        "session_id": "109910961642a185cb16873e388e2486",
                        "channel": "web_embarca_ai",
                        "operator_name": null,
                        "is_mobile": true,
                        "numberOfOptions": 0,
                        "origin_name": "JEQUIE - BA",
                        "destination_name": "TABOAO DA SERRA - SP"
                    }
                },
                "request_ip": "201.78.203.62",
                "request_user_agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36",
                "created_at": "2023-09-20T17:31:46.671+00:00"
            }
        }]"""

dictEx = [{'_index': 'data-production-2023-09-20', '_id': 'ZVGls4oBNkLSxFfA3kR4', '_score': 2.8663144, '_source': {'name': 'Seats', 'type': 'Integration', 'app_name': 
'sales-web', 'session_id': '109910961642a185cb16873e388e2486', 'payload': {'request': {'origin_id': '14760', 'destination_id': '584', 'date': '2023-11-01', 'operator_id': None, 'white_label_request': False, 'session_id': '109910961642a185cb16873e388e2486', 'channel': 'web_embarca_ai', 'operator_name': None, 'is_mobile': True, 'numberOfOptions': 0, 'origin_name': 'JEQUIE - BA', 'destination_name': 'TABOAO DA SERRA - SP'}}, 'request_ip': '201.78.203.62', 'request_user_agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36', 'created_at': '2023-09-20T17:31:46.671+00:00'}}]

filteredEx = [{'created_at': '2023-09-20T17:31:46.671+00:00', 'origin_id': '14760', 'distination_id': '584', 'date': '2023-11-01', 'operator_id': None, 'white_label_request': False, 'channel': 'web_embarca_ai', 'operator_name': None, 'is_mobile': True, 'numberOfOptions': 0, 'origin_name': 'JEQUIE - BA', 'destination_name': 'TABOAO DA SERRA - SP'}]

csvEx = f"""created_at{dictToCsvString.separator}origin_id{dictToCsvString.separator}distination_id{dictToCsvString.separator}date{dictToCsvString.separator}operator_id{dictToCsvString.separator}white_label_request{dictToCsvString.separator}channel{dictToCsvString.separator}operator_name{dictToCsvString.separator}is_mobile{dictToCsvString.separator}numberOfOptions{dictToCsvString.separator}origin_name{dictToCsvString.separator}destination_name{dictToCsvString.separator}
"2023-09-20T17:31:46.671+00:00"{dictToCsvString.separator}"14760"{dictToCsvString.separator}"584"{dictToCsvString.separator}"2023-11-01"{dictToCsvString.separator}null{dictToCsvString.separator}false{dictToCsvString.separator}"web_embarca_ai"{dictToCsvString.separator}null{dictToCsvString.separator}true{dictToCsvString.separator}0{dictToCsvString.separator}"JEQUIE - BA"{dictToCsvString.separator}"TABOAO DA SERRA - SP"{dictToCsvString.separator}"""

def main ():
    newDict = jsonToDict(jsonEx)

    plainDict = plainifyData(newDict)

    filteredList = filterKeys(plainDict)

    csvString = dictToCsvString.main(filteredList)

    if not newDict == dictEx:
        response = {
            "success": False,
            "response": "jsonToDict not working as expected!"
        }
    if not filteredList == filteredEx:
        response = {
            "success": False,
            "response": "plainifyData/filterKeys not working as expected!"
        }
    if not csvString == csvEx:
        response = {
            "success": False,
            "response": "dictToCsvString not working as expected!"
        }
    else: 
        response = {
            "success": True,
            "response": "Utils OK!"
        }

    return response