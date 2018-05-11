################################################
# File Name: findinD.py
# Author: ending19
# mail: ending19@163.com
# Created Time: Thu 10 May 2018 01:12:56 PM CST
#======================================
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import urllib.request
import urllib.parse
import random
import os


my_headers=["Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
]



def findinD(word, headers=my_headers):
    '''
    使用沪江小D来搜索单词，并返回html界面信息
    Args:
        word:       要搜索的字符串，要求是日语或汉字，非英文
        headers:    http访问时的Request的文件头列表
    Return:
        字符串形式的html信息
    '''
    URL = r'https://dict.hjenglish.com/jp/jc/'
    urlword = urllib.parse.quote(word) # url字符有要求，非英文的要处理
    url = URL + urlword

    random_header = {'User-Agent':random.choice(headers),
                    'Host':'dict.hjenglish.com',
                    'Referer':'https://dict.hjenglish.com/jp/'}

    req = urllib.request.Request(url=url, headers=random_header)
    res = urllib.request.urlopen(req)
    html = res.read().decode('utf-8')

    return html

