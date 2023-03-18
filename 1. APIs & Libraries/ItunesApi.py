# Demonstrates iterating over JSON

import json
import sys
import requests

if len(sys.argv) != 2:
    sys.exit()

#el limit medice cuantas canciones printeo

response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=35&term=" + sys.argv[1]
)
o = response.json()
for result in o["results"]:
    print(result["trackName"])
