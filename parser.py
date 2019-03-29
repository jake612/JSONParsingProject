import json
# Takes in a string from a file of JSON objects and returns list of jsonDict
def fileStrToJSONObjects(strPassed):
    jsonStrings = []
    strLen = len(strPassed)
    x = 0
    lastChar = ''
    newJSON = ''
    while x < strLen:
        if lastChar == '}' and strPassed[x] == '{':
            jsonStrings.append(newJSON)
            newJSON = ''
        else:
            lastChar = strPassed[x]
            newJSON += strPassed[x]
        x += 1

    jsonObj = []
    for j in jsonStrings:
        jsonObj.append(json.loads(j))

    return jsonObj

def parseByLine(fileObj):
    jsonDict = []
    for i in fileObj:
        jsonDict.append(json.loads(i))
    return jsonDict

# opening a file to string fo
filename = input("Enter a file name to parse\n")
fo = open(filename, "r")

# create a dictionary from JSON file
jsonDict = parseByLine(fo)

