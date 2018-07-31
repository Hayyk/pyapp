import json

textFromSlack="this is sample sentence to split"
params=textFromSlack.split()
with open ("root.json") as rj:
    data=json.load(rj)
for param in params:
    for t in data['tests']:
        if t['test'] == param:
            urlToUse=t['url']
            print(param)
            print(urlToUse)
#           runsomefunction(param, urlToUse)
            print("this is what I needed")
