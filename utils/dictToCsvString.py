import json
separator = ","

def dictToCsvString(oldDict):
    entries = []

    for item in oldDict:
        for key in item.keys():
            if not key in entries:
                entries.append(key)

    result = ""

    for i, item in enumerate(entries):
        result += item + (separator if i + 1 < len(entries) else '')

    for item in oldDict:
        result += '\n'
        for i, key in enumerate(entries):
            itemEntries = item.keys()
            if key in itemEntries:
                result += str(item[key]) + (separator if i + 1 < len(entries) else '')
            else:
                result += separator

    return result