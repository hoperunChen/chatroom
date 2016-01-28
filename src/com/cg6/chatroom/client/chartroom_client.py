'''
Created on 2016-1-27

@author: cr
'''
from com.cg6.utils.conf_reader_util import ConfReader
import socket,threading,time

class ChartroomClient:
    
    def __init__(self):
        self.clientName = 'guest'
        cr = ConfReader()
        self._ipaddr = cr.get('ipaddr')
        self._port = int(cr.get('port'))
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    
    def __connect(self):
        self._socket.connect((self._ipaddr, self._port))
    
    def __receive(self):
        def recv(socket):
            while True:
                print socket.recv(1024)
                time.sleep(1)
        threading.Thread(target=recv, args=(self._socket))
        
    def start(self):
        self.clientName = raw_input('Please enter your nickname:')
        self.__connect()
        self.__receive()
        while True:
            msg = raw_input('say something')
            self._socket.send(msg)
            time.sleep(1)
        
if __name__ == '__main__':
    cc = ChartroomClient()
    cc.start()
    