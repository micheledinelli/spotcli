import re
import os

def clear_cache():
    for f in os.listdir('./'):
        if re.search('^\.cache', f):
            os.remove(f)