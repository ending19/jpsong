################################################
# File Name: songslice.py
# Author: ending19
# mail: ending19@163.com
# Created Time: Thu 10 May 2018 10:53:14 PM CST
#======================================
# !/usr/bin/env python3
# -*- coding: utf-8 -*-


import re
from findinD import findinD


jp_qing_ping = ['あ', 'い', 'う', 'え', 'お', 'か', 'き', 'く', 'け', 'こ', 'さ', 'し', 'す', 'せ', 'そ', 'た', 'ち', 'つ', 'て', 'と', 'な', 'に', 'ぬ', 'ね', 'の', 'は', 'ひ', 'ふ', 'へ', 'ほ', 'ま', 'み', 'む', 'め', 'も', 'や', 'ゆ', 'よ', 'ら', 'り', 'る', 'れ', 'ろ', 'わ', 'を', 'ん']
jp_qing_pian = ['ア', 'イ', 'ウ', 'エ', 'オ', 'カ', 'キ', 'ク', 'ケ', 'コ', 'サ', 'シ', 'ス', 'セ', 'ソ', 'タ', 'チ', 'ツ', 'テ', 'ト', 'ナ', 'ニ', 'ヌ', 'ネ', 'ノ', 'ハ', 'ヒ', 'フ', 'ヘ', 'ホ', 'マ', 'ミ', 'ム', 'メ', 'モ', 'ヤ', 'ユ', 'ヨ', 'ラ', 'リ', 'ル', 'レ', 'ロ', 'ワ', 'ヲ', 'ン']
jp_qing_yin = ['a', 'i', 'u', 'e', 'o', 'ka', 'ki', 'ku', 'ke', 'ko', 'sa', 'shi', 'su', 'se', 'so', 'ta', 'chi', 'tsu', 'te', 'to', 'na', 'ni', 'nu', 'ne', 'no', 'ha', 'hi', 'fu', 'he', 'ho', 'ma', 'mi', 'mu', 'me', 'mo', 'ya', 'yu', 'yo', 'ra', 'ri', 'ru', 're', 'ro', 'wa', 'wo', 'n']

jp_zhu_ping = ['が', 'ぎ', 'ぐ', 'げ', 'ご', 'ざ', 'じ', 'ず', 'ぜ', 'ぞ', 'だ', 'ぢ', 'づ', 'で', 'ど', 'ば', 'び', 'ぶ', 'べ', 'ぼ']
jp_zhu_pian = ['ガ', 'ギ', 'グ', 'ゲ', 'ゴ', 'ザ', 'ジ', 'ズ', 'ゼ', 'ゾ', 'ダ', 'ヂ', 'ヅ', 'デ', 'ド', 'バ', 'ビ', 'ブ', 'ベ', 'ボ']
jp_zhu_yin = ['ga', 'gi', 'gu', 'ge', 'go', 'za', 'ji', 'zu', 'ze', 'zo', 'da', 'ji', 'zu', 'de', 'do', 'ba', 'bi', 'bu', 'be', 'bo']

jp_hzhu_ping = ['ぱ', 'ぴ', 'ぷ', 'ぺ', 'ぽ']
jp_hzhu_pian = ['パ', 'ピ', 'プ', 'ペ', 'ポ']
jp_hzhu_yin = ['pa', 'pi', 'pu', 'pe', 'po']

jp_ao_ping = ['きゃ', 'きゅ', 'きょ', 'ぎゃ', 'ぎゅ', 'ぎょ', 'しゃ', 'しゅ', 'しょ', 'じゃ', 'じゅ', 'じょ', 'ちゃ', 'ちゅ', 'ちょ', 'ぢゃ', 'ぢゅ', 'ぢょ', 'にゃ', 'にゅ', 'にょ', 'ひゃ', 'ひゅ', 'ひょ', 'びゃ', 'びゅ', 'びょ', 'ぴゃ', 'ぴゅ', 'ぴょ', 'みゃ', 'みゅ', 'みょ', 'りゃ', 'りゅ', 'りょ']
jp_ao_pian = ['キャ', 'キュ', 'キョ', 'ギャ', 'ギュ', 'ギョ', 'シャ', 'シュ', 'ショ', 'ジャ', 'ジュ', 'ジョ', 'チャ', 'チュ', 'チョ', 'ヂャ', 'ヂュ', 'ヂョ', 'ニャ', 'ニュ', 'ニョ', 'ヒャ', 'ヒュ', 'ヒョ', 'ビャ', 'ビュ', 'ビョ', 'ピャ', 'ピュ', 'ピョ', 'ミャ', 'ミュ', 'ミョ', 'リャ', 'リュ', 'リョ']
jp_ao_yin = ['kya', 'kyu', 'kyo', 'gya', 'gyu', 'gyo', 'sha', 'shu', 'sho', 'jya', 'jyu', 'jyo', 'cha', 'chu', 'cho', 'dya', 'dyu', 'dyo', 'nya', 'nyu', 'nyo', 'hya', 'hyu', 'hyo', 'bya', 'byu', 'byo', 'pya', 'pyu', 'pyo', 'mya', 'myu', 'myo', 'rya', 'ryu', 'ryo']


jp_special = ['ィ', 'ェ', 'ょ', 'ァ', 'ゅ', 'ョ', 'ャ', 'ォ', 'ゃ','ゥ','ュ', 'っ']

jp_sign = ['\u3000', '・', '「', '」', '、']

for i in range(32,127):
    jp_sign.append(chr(i))


jp_ping = jp_qing_ping + jp_zhu_ping + jp_hzhu_ping
jp_pian = jp_qing_pian + jp_zhu_pian + jp_hzhu_pian

jp_check = jp_ping + jp_pian + jp_special + jp_sign

re_find_pronounces = re.compile(r'<div class="pronounces">\s*<span>\[(.*)\]</span>', re.L|re.M)
re_findsec = re.compile(r'你想查的是不是: </h2>\s*<ul>\s*(.*?)</ul>',re.L|re.M|re.S)
re_findwords = re.compile(r'<li><a href="/jp/jc/.*?>(.*)</a></li>',re.L|re.M)

def songslice(line):
    songlrc = ''
    songlist = []
    rest = line
    while True:
        for i,ch in enumerate(rest):
            if ch not in jp_check:
                break
            i = i + 1
        songlist.append(rest[:i])
        rest = rest[i:]
       # print(rest)
        if rest == '':
            break
        if len(rest.strip('\n')) >= 2:
            word = rest[:2]
            pro, sec = findinHTML(word)
            if pro != []:
                songlist.append(pro[-1])
                rest = rest[2:]
                continue
            elif sec != []:
                word = ''
                for s in sec:
                    if s in rest:
                        if len(s) > len(word):
                            word = s
                if word != '':
                    pro,sec = findinHTML(word)
                    if pro != []:
                        songlist.append(pro[-1])
                        rest = rest[len(word):]
                        continue
        word = rest[:1]
        if word == '\n':
            songlist.append(word)
        else:
            pro = findinHTML(word)[0]
            if pro != []:
                songlist.append(pro[0])
            else:
                songlist.append(word)
        rest = rest[1:]
    for s in songlist:
       songlrc = songlrc + s
    return songlrc


def findinHTML(word):
    html = findinD(word)
    pro = re_find_pronounces.findall(html)
    m = re_findsec.findall(html)
    if m != []:
        sec = re_findwords.findall(m[0])
    else:
        sec = []
    return pro, sec


if __name__ == "__main__":
    line = 'キラリ光るHope'
    print(songslice(line))

