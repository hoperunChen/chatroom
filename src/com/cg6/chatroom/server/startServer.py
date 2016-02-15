'''
Created on 2016-1-27

@author: cr
'''
from com.cg6.chatroom.server import chatroom_server

if __name__ == '__main__':
    cs = chatroom_server.ChatroomServer('chat room')
    cs.start()