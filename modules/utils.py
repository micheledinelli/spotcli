import re
import os
import json

from pygments import highlight, lexers, formatters

def clear_cache():
    '''
    Clear cached Spotify tokens in the current directory.

    This function searches for files starting with '.cache' in the current directory and removes them.

    Note: Be cautious when using this function, as it permanently deletes cache files.

    Returns:
    - None
    '''
    # Iterate through files in the current directory
    for f in os.listdir('./'):
        # Check if the file name matches the pattern '^\.cache'
        if re.search('^\.cache', f):
            # Remove the cache file
            os.remove(f)

def pretty_print_json(json_str):
    formatted_json = json.dumps(json_str, sort_keys=True, indent=2)
    colorful_json = highlight(formatted_json, lexers.JsonLexer(), formatters.TerminalFormatter())
    print(colorful_json)