'''
Created on 2016-1-27

@author: cr
'''
from com.cg6.chatroom.server.SocketServer import SocketServer

class ChatroomServer(SocketServer):
    '''
    ChatroomServer
    '''
    def __init__(self, chatRoomName):
        super(ChatroomServer,self).__init__()
    
    def connNewClient(self,sock, addr):
        pass
    
    def receive(self,data,clientSock, clientAddr):
        clientSock.send('hello')
        
