import json
from pygments import highlight, lexers, formatters

def pprint(json_str):
    formatted_json = json.dumps(json_str, sort_keys=True, indent=2)
    colorful_json = highlight(formatted_json, lexers.JsonLexer(), formatters.TerminalFormatter())
    print(colorful_json)