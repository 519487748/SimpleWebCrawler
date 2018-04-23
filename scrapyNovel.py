#!/user/bin/env python
# _*_coding:utf-8_*_

import requests
from bs4 import BeautifulSoup
import os
import time
from multiprocessing import Pool

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
}


def get_html(url):
    try:
        # 获取小说某一章的html
        r = requests.get(url, headers=headers, timeout=120)
        r.encoding = r.apparent_encoding
        novel_html = r.text
        get_text(novel_html)
    except:
        print("html获取失败")


def get_text(html):
    # bs4分析，提取内容和标题
    soup = BeautifulSoup(html, 'lxml')
    text = soup.find('div', id='content').text
    title = soup.h1.string
    # 保存到本地
    root = "E://novels//"
    path = root + title
    print("正在保存：" + title)
    if not os.path.exists(root):
        os.mkdir(root)
    with open(path + r'.txt', 'a', encoding='utf8') as f:
        f.write(text + '\n\n')
        f.close()


if __name__ == '__main__':

    start = time.clock()
    root_url = "http://www.booktxt.net/2_2082/"
    urlList = []
    for each in range(1, 21):
        text_url = root_url + str(677715 + each) + ".html"
        urlList.append(text_url)

    pool = Pool(processes=10)
    pool.map(get_html, urlList)
    pool.close()
    pool.join()

    end = time.clock()
    print("共用了：%f" % (end - start))



