import os
import requests

def get_droplets():
    url = 'https://jsonplaceholder.typicode.com/posts'
    r = requests.get(url, headers={'Authorization':'Bearer %s' % os.getenv('JWT')})
    droplets = r.json()
    return droplets
