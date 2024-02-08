import json
from pygments import highlight, lexers, formatters
from pathlib import Path
import os

def pprint(json_str):
    formatted_json = json.dumps(json_str, sort_keys=True, indent=2)
    colorful_json = highlight(formatted_json, lexers.JsonLexer(), formatters.TerminalFormatter())
    print(colorful_json)

USERDATA_PATH = os.path.abspath(
    os.path.expanduser("~/.config/spoticli/userdata.json"))

class DataFile(object):

    def __init__(self, pathStr, defaultContents={}):
        self.path = Path(pathStr)
        
        # create file
        if not self.path.parent.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
        
        if not self.path.exists():
            self.write(defaultContents)
        
        # update contents if new defaut values have been added
        currContents = self.read()
        for key in defaultContents:
            if key not in currContents:
                currContents[key] = defaultContents[key]
        
        self.write(currContents)

    def read(self):
        with open(self.path, "r+") as file:
            contents = json.load(file)
        return contents

    def write(self, contents):
        with open(self.path, "w+") as file:
            json.dump(contents, file, indent=4)

    def set(self, key, value):
        contents = self.read()
        contents[key] = value
        self.write(contents)

    def get(self, key, default=False):
        contents = self.read()
        if key not in contents:
            return default
        return contents[key]

class CacheFile(DataFile):

    def __init__(self, path, defaultContents={}):
        super().__init__(path, defaultContents)

    def isCached(self, key):
        contents = self.read()
        return key in contents

    def clear(self):
        self.write({})

userdata = DataFile(USERDATA_PATH)
