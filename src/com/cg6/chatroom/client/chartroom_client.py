'''
Created on 2016-1-27

@author: cr
'''
from com.cg6.utils.conf_reader_util import ConfReader
from com.cg6.chatroom import constants
import socket, threading, time

class ChartroomClient:
    
    def __init__(self):
        self.clientName = 'guest'
        cr = ConfReader()
        self._ipaddr = cr.get('ipaddr')
        self._port = int(cr.get('port'))
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._isInited = False
    
    def __connect(self):
        self._socket.connect((self._ipaddr, self._port))
        self.setName()
    
    def __receive(self):
        t = threading.Thread(target=self.recv, args=(self._socket,))
        t.start()
        
    def recv(self, socket):
        while True:
            data = socket.recv(1024)
            print '\n' + data
            time.sleep(1)
            
    def setName(self):
        self.clientName = raw_input('Please enter your nickname:')
        self._socket.send(constants.FN_SEPARATOR+self.clientName)
        
    def start(self):
        self.__connect()
        self.__receive()
        while True:
            if self._isInited:
                msg = raw_input('')
                self._socket.send(msg)
            time.sleep(1)
        
if __name__ == '__main__':
    cc = ChartroomClient()
    cc.start()
    
