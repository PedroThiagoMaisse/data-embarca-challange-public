import datetime
from services.getBucketData import getBucketData
from services.bucketPutObject import postBucketData


def main ():
    try:
        now = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        
        postBucketData('temp/testing/bucket.txt', now)    

        returnValue = getBucketData('temp/testing/bucket.txt')
        
        if (returnValue != now):
            response = {
                "success": False,
                "response": "Troca de informação com o bucket não respondeu o esperado!"
            }
        else:
            response = {
                "success": True,
                "response": "Services OK!"
            }

        return response
    except:
        return {
            "success": False,
            "response": "Erro no Service!"
        }