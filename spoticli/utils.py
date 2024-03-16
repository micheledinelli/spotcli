import json
from pygments import highlight, lexers, formatters
from pathlib import Path
import os

CLIENT_ID="a80867c5ce9640d4888f52ac2223df83"
CLIENT_SECRET="eca83a36fb8c4ebdbbc1ace8d6b7deb2"
SCOPE="user-read-playback-state user-modify-playback-state user-library-read"
REDIRECT_URI="http://localhost:8081"

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

    def delete(self, key):
        contents = self.read()
        del contents[key]
        self.write(contents)

class CacheFile(DataFile):

    def __init__(self, path, defaultContents={}):
        super().__init__(path, defaultContents)

    def isCached(self, key):
        contents = self.read()
        return key in contents

    def clear(self):
        self.write({})

userdata = DataFile(USERDATA_PATH)
