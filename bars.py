import json
import pprint

with open('bars.json', 'r') as f:
    bars = json.load(f)

pprint(bars)