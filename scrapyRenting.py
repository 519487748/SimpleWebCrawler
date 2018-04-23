#!/user/bin/env python
# _*_coding:utf-8_*_

import requests
from bs4 import BeautifulSoup

def get_html(url):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0"
    }
    r = requests.get(url, headers=headers, timeout=30)
    r.encoding = r.apparent_encoding
    return r.text


def get_rent_info(html):
    soup = BeautifulSoup(html, 'html.parser')
    rent_class = soup.findAll(class_='zu-info')
    for i in range(len(rent_class)):
        print(rent_class[i].a.attrs['title'], rent_class[i].a.attrs['href'], '\n')



def main():
    base_url = "https://bj.zu.anjuke.com/"
    base_html = get_html(base_url)
    get_rent_info(base_html)

main()