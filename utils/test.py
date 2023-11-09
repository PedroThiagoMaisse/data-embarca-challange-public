import utils.jsonToDict as jsonToDict 
import utils.dictToCsvString as dictToCsvString
import utils.plainify as plainify
import services.getBucketData as getBucketData
import services.bucketPutObject as bucketPutObject

jsonEx = getBucketData.getBucketData('input/inp_2023-09-20T14-29-57-ec.json')

dictEx = [
    {
        "id": "file",
        "value": "File",
        "popup": "menuitem"
    }
]

csvEx = f"""id{dictToCsvString.separator}value{dictToCsvString.separator}popup{dictToCsvString.separator}
"file"{dictToCsvString.separator}"File"{dictToCsvString.separator}"menuitem"{dictToCsvString.separator}"""

def main ():
    newDict = jsonToDict.jsonToDict(jsonEx)['hits']

    plainDict = plainify.plainifyData(newDict)
    csvString = dictToCsvString.main(newDict)

    x = bucketPutObject.postBucketData('teste/001.csv', csvString)

    # if dictEx != newDict:
    #     response = {
    #         "success": False,
    #         "response": "JSON não bate com o Dict"
    #     }
    # elif csvEx != csvString:
    #     response = {
    #         "success": False,
    #         "response": "Dict não bate com o csv"
    #     }
    # else:
    response = {
        "success": True,
        "response": "Utils OK!"
    }
    return response