import json
import re

def resolveJson(path):
    file = open(path, "r+")
    for line in file:
        print line
        p1 = re.compile(r'[/](.*)[/]')
        hashes = re.search(p1, line)
        print hashes

resolveJson("items.json")