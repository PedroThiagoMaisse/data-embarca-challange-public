def filterKeys (array):
    entries = [
        {"current": "_source_created_at", "new": "created_at"},
        {"current": "_source_payload_request_origin_id", "new": "origin_id"},
        {"current": "_source_payload_request_destination_id", "new": "distination_id"},
        {"current": "_source_payload_request_date", "new": "date"},
        {"current": "_source_payload_request_operator_id", "new": "operator_id"},
        {"current": "_source_payload_request_white_label_request", "new": "white_label_request"},
        {"current": "_source_payload_request_channel", "new": "channel"},
        {"current": "_source_payload_request_operator_name", "new": "operator_name"},
        {"current": "_source_payload_request_is_mobile", "new": "is_mobile"},
        {"current": "_source_payload_request_numberOfOptions", "new": "numberOfOptions"},
        {"current": "_source_payload_request_origin_name", "new": "origin_name"},
        {"current": "_source_payload_request_destination_name", "new": "destination_name"}
        ]

    returnList = []

    for item in array:
        newItem = {}
        for keys in entries:
            if item[keys['current']] != 'null' and item[keys['current']] != None:
                newItem[keys['new']] = item[keys['current']]
            else:
                newItem[keys['new']] = ''
        returnList.append(newItem)

    return returnList    