#!/usr/bin/python
#coding=utf-8

from socket import *

def client():
    while True:
        sock = socket(AF_INET,SOCK_STREAM)
        sock.connect(('127.0.0.1',8888))
        print '������Ҫ���͵��ַ�����'
        buf = raw_input()
        sock.send(buf)
        print sock.recv(1024)
        sock.close()

if __name__=="__main__":
    client()
