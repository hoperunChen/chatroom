'''
Created on 2016-1-27

@author: cr
'''

import ConfigParser  
import path_utils

class ConfReader(object):
    def __init__(self,path=path_utils.getConfPath()+'app.conf'):
        self.confPath =  path
        self.config = ConfigParser.ConfigParser()
        with open(self.confPath,'r') as cfgfile:
            self.config.readfp(cfgfile)
            
    def get(self,option,section='default'):
        return self.config.get(section, option)
    

cr = ConfReader()
print cr.get('ipaddr')





