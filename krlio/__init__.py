import requests
from bs4 import BeautifulSoup

krl_base = 'http://krl.io' # TODO api root?

class KrlExcpetion(Exception):
    pass

def get_link(code):
    r = requests.get('http://krl.io/{}'.format(code), allow_redirects=False)
    if not r.status_code == 301:
        raise KrlException('Link not found')
    return r.headers['location']

def make_anon_link(url):
    # simple - take what krl gave us
    r = requests.post('http://krl.io/krl.php', data={"url":url})

    if not r.status_code == 200:
        raise KrlException('Could not create anon link!')

    soup = BeautifulSoup(r.content, 'html.parser')
    return soup.input['value']
