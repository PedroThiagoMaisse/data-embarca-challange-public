def plainifyDataList(list):
    result = []
    for item in list:
        x = plainifyDict(item, '')
        result.append(x)

    return result
        

def plainifyDict(dit, str):
    result = {}
    compl = str + '_' if str != '' else ''
    for key in dit:
        if type(dit[key]) is dict:
            result.update(plainifyDict(dit[key], compl + key))
        else:
            result[compl + key] = dit[key]

    return result

