'''
Created on 27-03-2013

@author: waf3l
'''
import subprocess
import os

class GuiConvert(object):
    '''
    This class is for converting files from ui to py
    '''
    def __init__(self,params):
        '''
        Constructor
        '''
        self.inputFile = params
    
    def convertGuiFile(self):
        fileName = os.path.basename(self.inputFile)
        print os.path.splitext(fileName)[1]
        if os.path.splitext(fileName)[1] == '.ui':
            
            path = os.path.split(self.inputFile)[0]
            pythonGuiFile = os.path.splitext(fileName)[0]+'.py'
            print "file name is: ",fileName
            print "path is: ",path
            print "Out put file is: ", pythonGuiFile
            p = subprocess.Popen(["pyside-uic", self.inputFile, '-o', path+'/'+pythonGuiFile])
            (output, err) = p.communicate()
            print 'Output from pyside: ', output 
            return True  
        else:
            print "This is not UI file: ",fileName
            return False
        