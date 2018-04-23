#!/user/bin/env python
# _*_coding:utf-8_*_

import requests
import os

url = "https://m.360buyimg.com/babel/jfs/t18658/130/1685735212/98555/9c1f9df6/5ad47c74Na502d29e.jpg"
root = "E://pics//"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("图片保存cg")
    else:
        print("保存失败")
except:
    print("爬取失败")
