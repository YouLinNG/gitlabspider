import json
import re

# find the first []
# def resolveJson(path):
#     file = open(path, "rb")
#     fileJson = json.load(file)
#     fileStr = json.dumps(fileJson)
#     print fileStr
#     p1 = re.compile(r'[[](.*?)[]]', re.S)
#     build_result = re.search(p1, fileStr[1:-1]).group()
#     print build_result

def resolveJson(path):
    file = open(path, "rb")
    for line in file:
        print line
        p1 = re.compile(r'[[](.*?)[]]')
        build_result = re.match(p1, line)
        print build_result


resolveJson("items.json")