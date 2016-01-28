'''
Created on 2016-1-27

@author: cr
'''

import os,sys


def getProjectName():
    absPath=os.path.abspath(sys.argv[0]) 
    absPath=os.path.dirname(absPath)+"/" 
    absPath = absPath[0:absPath.find('\\src\\')]
    return absPath

def getConfPath():
    absPath=os.path.abspath(sys.argv[0]) 
    absPath=os.path.dirname(absPath)+"/" 
    absPath = absPath[0:absPath.find('\\src\\')]
    return absPath+'/resources/'