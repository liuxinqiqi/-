#!/usr/bin/python
#coding=utf-8

import urllib
import re

def getHtml(url):
    page = urllib.urlopen(url)  #��һ��url
    html = page.read()  #��ȡȫ����������һ���ַ���
    return html

def getImg(html):
    reg = r'src="(http://.+?\.jpg)"'
    
    imgre = re.compile(reg)   # ��һ��������ʽ����Ϊ��Ӧ�Ķ���
    imglist = re.findall(imgre,html) # ��html�ַ������ҵ�����imgre������ʽ�������һ���б�
    print(imglist)

    x = 0

    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.jpg'%x)  #����������ȡ�ر��ز���������
        x+=1

html = getHtml('http://tieba.baidu.com/p/4229162765')

print (getImg(html))

