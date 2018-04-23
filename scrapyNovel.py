#!/user/bin/env python
# _*_coding:utf-8_*_

import requests
from bs4 import BeautifulSoup
import os


def get_html(url):

    r = requests.get(url, headers={'Connection': 'close'}, timeout=30)
    r.encoding = r.apparent_encoding
    html = r.text
    return html


def get_text(html):

    soup = BeautifulSoup(html, 'html.parser')
    text = soup.find('div', id='content').text

    root = "E://novels//"
    path = root + "校花的贴身高手"
    if not os.path.exists(root):
        os.mkdir(root)
    with open(path + r'.txt', 'a', encoding='utf8') as f:
        f.write(text + '\n\n')
        f.close()


def main():

    root_url = "http://www.booktxt.net/2_2082/"
    for i in range(1, 3):
        text_url = root_url + str(677715 + i) + ".html"
        text_html = get_html(text_url)
        get_text(text_html)


main()
