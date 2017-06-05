import requests

KRL_BASE = 'http://krl.io/v1/'

class KrlException(Exception):
    pass

def get_version():
    r = requests.get(KRL_BASE + 'version')
    if not r.status_code == 200:
        return KrlException('Could not get version: {}'.format(r.staus_code))
    return r.json()['version']

def get_link(code):
    r = requests.get(KRL_BASE+'link/{}'.format(code))
    if not r.status_code == 200:
        return KrlException('Link not found!')
    return r.json()['url']

def make_anon_link(url):
    r = requests.post(KRL_BASE+'link/{}'.format(url))
    if not r.status_code == 200:
        return KrlException('Could not shorten link: {}'.format(r.status_code))
    return r.json()['url']
