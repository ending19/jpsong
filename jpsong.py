################################################
# File Name: jpsong.py
# Author: ending19
# mail: ending19@163.com
# Created Time: Tue 08 May 2018 07:56:05 PM CST
#======================================
# !/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
import re
from songslice import songslice


def jpsong():
    ''' 打开txt文件，对其中的汉字变成假名形式，并保存'''
    songpath = sys.argv[1]
    spath = songpath[:-3]+'lrc'

    try:
        f = open(songpath, 'r')
    except IOError:
        print('No such file!')
        sys.exit(1)

    songlrc = ""
    for line in f.readlines():
        temp = songslice(line)
        print(temp)
        songlrc = songlrc + temp

    f.close()

    with open(spath,'w') as f:
        f.write(songlrc)


if __name__ == "__main__":
    jpsong()
