import requests
from bs4 import BeautifulSoup

def get_page_text(url):
    html_page = requests.get(url).content
    soup = BeautifulSoup(html_page, 'lxml')

    whitelist = ['p', 'strong', 'em', 'b', 'u', 'i', 'h1', 'h2', 'h3']
    out = ""

    for t in soup.find_all(text=True):
        if t.parent.name in whitelist:
            out += '{} '.format(t)

    escape = ['\r', '\n', '\t', '\xa0']

    for e in escape:
        out = out.replace(e, '')

    return out
