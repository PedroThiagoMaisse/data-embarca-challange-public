import json
separator = ";"

def main(oldDict):
    entries = []

    for item in oldDict:
        for key in item.keys():
            if not key in entries:
                entries.append(key)

    result = ""

    for item in entries:
        result += item + separator

    for item in oldDict:
        result += '\n'
        for key in entries:
            if item[key]:
                result += json.dumps(item[key]) + ";"
            else:
                result += ";"

    return result