'''
Created on 2016-1-27

@author: cr
'''
from com.cg6.utils.conf_reader_util import ConfReader
from abc import abstractmethod,ABCMeta
import socket,threading,time

class SocketServer(object):
    
    __metaclass__ = ABCMeta

    def __init__(self):
        cr = ConfReader()
        self._ipaddr = cr.get('ipaddr')
        self._port = int(cr.get('port'))
        self._maxConn = int(cr.get('max_conn'))
        self._server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self._server.bind((self._ipaddr,self._port))
        self._server.listen(self._maxConn)
        
    def start(self):
        while True:
            print 'chat room Service begin start'
            clientSock, clientAddr = self._server.accept()
            t = threading.Thread(target=self.tcpLink, args=(clientSock, clientAddr))
            print 'chat room Service has bean start'
            t.start()
            
    
    def tcpLink(self,clientSock, clientAddr):
        print 'Accept new connection from %s:%s...' %(clientAddr)
        #TODO add client
        self.connNewClient(clientSock, clientAddr)
        clientSock.send('Welcome!')
        while True:
            data = clientSock.recv(1024) 
            time.sleep(1)
            if data == 'exit' or not data:
                break
            print 'receive message from %s:%s;-->%s' %(clientAddr[0],clientAddr[1],data)
            self.receive(data,clientSock, clientAddr)
            #send everyOne
            #clientSock.send('hello %s' % data)
        clientSock.close()
        print 'Connection from %s:%s closed.' %(clientAddr)
    
    @abstractmethod
    def connNewClient(self,sock, addr):
        pass
    @abstractmethod
    def receive(self,data,clientSock, clientAddr):
        pass
        
        