import utils.jsonToDict as jsonToDict 
import utils.dictToCsvString as dictToCsvString

jsonEx = """[
    {
        "id": "file",
        "value": "File",
        "popup": "menuitem"
    }
]"""

dictEx = [
    {
        "id": "file",
        "value": "File",
        "popup": "menuitem"
    }
]

csvEx = """id;value;popup;
"file";"File";"menuitem";"""

def main ():
    newDict = jsonToDict.jsonToDict(jsonEx)
    csvString = dictToCsvString.main(newDict)

    if dictEx != newDict:
        response = {
            "success": False,
            "response": "JSON não bate com o Dict"
        }
    elif csvEx != csvString:
        response = {
            "success": False,
            "response": "Dict não bate com o csv"
        }
    else:
        response = {
            "success": True,
            "response": "Utils OK!"
        }
    return response