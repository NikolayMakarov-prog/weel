import urllib.request
import json


def get(url):
    response = urllib.request.urlopen(url)
    request = response.read()
    return json.loads(request)