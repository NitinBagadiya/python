import itertools 
import json 
from urllib.request import urlopen

with urlopen("https://www.googleapis.com/youtube/v3/channels?part=contentDetail") as response:
    data=response.read()

print(data)