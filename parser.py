import json
import matplotlib.pyplot as plt
# Takes in a file object and returns a list containing a dictionary for each JSON
def parseByLine(fileObj):
    jsonDict = []
    for i in fileObj:
        jsonDict.append(extractAttributes(json.loads(i)))
    return jsonDict

# Takes in a JSON Tweet dictionary and returns dictionary of pertinent
def extractAttributes(dictObj):
    newDict = {}
    newDict['id'] = dictObj.get('id')
    newDict['created_at'] = dictObj.get('created_at')
    newDict['in_reply_to_status_id'] = dictObj.get('in_reply_to_status_id')
    newDict['retweet_count'] = dictObj.get('retweet_count')
    newDict['lang'] = dictObj.get('lang')
    newDict['hashtags'] = len(dictObj.get('entities').get('hashtags'))
    newDict['urls'] = len(dictObj.get('entities').get('urls'))
    newDict['user_mentions'] = len(dictObj.get('entities').get('user_mentions'))
    newDict['followers_count'] = dictObj.get('user').get('followers_count')
    newDict['friends_count'] = dictObj.get('user').get('friends_count')
    newDict['listed_count'] = dictObj.get('user').get('listed_count')
    newDict['verified'] = dictObj.get('user').get('verified')
    newDict['statuses_count'] = dictObj.get('user').get('statuses_count')
    newDict['time_zone'] = dictObj.get('user').get('time_zone')
    return newDict


# opening a file to string fo
filename = input("Enter a file name to parse\n")
fo = open(filename, "r")

# create a dictionary from JSON file
jsonDict = parseByLine(fo)
fo.close()

i = 0
while i < 100:
    print(jsonDict.pop(i)['friends_count'])

    i += 1
