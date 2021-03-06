'''
Created on 2016-1-27

@author: cr
'''
from com.cg6.chatroom.server import socket_server
from com.cg6.chatroom import constants

class ChatroomServer(socket_server.SocketServer):
    '''
    ChatroomServer
    '''
    
    KEY_CLIENT_SOCK = 'sock'
    KEY_CLIENT_ADDR = 'addr'
    KEY_CLIENT_NICKNAME = 'nickName'
    
    def __init__(self, chatRoomName):
        super(ChatroomServer,self).__init__()
        self.clientList = {}
    
    def connNewClient(self,sock, addr):
        self.clientList[addr] = {self.KEY_CLIENT_SOCK:sock,self.KEY_CLIENT_ADDR:addr,self.KEY_CLIENT_NICKNAME:'nickName'}
    
    def receive(self,data,clientSock, clientAddr):
        if data.find(constants.FN_SEPARATOR)==0:
            name = data[data.find(constants.FN_SEPARATOR)+len(constants.FN_SEPARATOR):len(data)]
            self.clientList[clientAddr]['nickName'] = name
            clientSock.send('hello '+name)
            clientSock.send(constants.FN_SEPARATOR+'ok')
        else:
            for client in self.clientList.values():
                client['sock'].send(self.clientList[clientAddr][self.KEY_CLIENT_NICKNAME]+':'+data)
        
