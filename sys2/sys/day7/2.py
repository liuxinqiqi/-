#!/usr/bin/python
#coding=utf-8

from twisted.internet import protocol,reactor
from time import ctime

PORT = 8888

class TSservProtocol(protocol.Protocol):
    def connectionMade(self):                  #��дԭ�����еĺ������пͻ���ʱ������
        clnt = self.clnt = self.transport.getPeer().host
        print "...connected from:",clnt
    def dataReceived(self,data):               #��ͻ��˽����������ݴ���ʱ������
        self.transport.write('[%s] %s'%(ctime(),data))

factory = protocol.Factory()     #����protocol������ÿ�����ӽ�������һ������
factory.protocol = TSservProtocol # ��������ִ�е���

print "waiting for connection..."
reactor.listenTCP(PORT,factory)  # ���м������пͻ������Ӻ󴴽�һ��TSserv����������
reactor.run()
