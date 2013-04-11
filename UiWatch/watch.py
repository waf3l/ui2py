'''
Created on 27-03-2013
@author: waf3l

The code for class UiWatch/watch.py and EventHandler is from
--ThreadedNotifier example from tutorial
--
--See: http://github.com/seb-m/pyinotify/wiki/Tutorial

Usage:
Options:
    -h, --help display this message
    -i, --input <the path to dir or path with file name to watch>
    
Example of usage:
    ui2py.py -i /home/user/Project/Ui
    ui2py.py -i /home/user/Project/Ui/MainWindow.ui
    ui2py.py --input /home/user/Project/Ui
    ui2py.py --input /home/user/Project/Ui/MainWindow.ui

'''
from UiConvert import convert
import pyinotify
import getopt, sys


mask = pyinotify.IN_CLOSE_WRITE  # watched events @UndefinedVariable

class EventHandler(pyinotify.ProcessEvent):

    def __init__(self, parent):
        self.parent = parent

    def process_IN_CREATE(self, event):
        #print "Creating:", event.pathname
        pass
    
    def process_IN_DELETE(self, event):
        #print "Removing:", event.pathname
        pass
    
    def process_IN_ACCESS(self, event):
        #print "ACCESS event:", event.pathname
        pass
    
    def process_IN_ATTRIB(self, event):
        #print "ATTRIB event:", event.pathname
        pass
    
    def process_IN_CLOSE_NOWRITE(self, event):
        #print "CLOSE_NOWRITE event:", event.pathname
        pass
    
    def process_IN_CLOSE_WRITE(self, event):
        #print "CLOSE_WRITE event:", event.pathname
        self.parent.convertGui(event.pathname)
        
    def process_IN_MODIFY(self, event):
        #print "MODIFY event: ", event.pathname
        pass
    
    def process_IN_OPEN(self, event):
        #print "OPEN event:", event.pathname
        pass
    
class MyWatcher():
    '''
    Watcher class
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.wm = pyinotify.WatchManager()
        self.eh = EventHandler(self) 
        self.notifier = pyinotify.ThreadedNotifier(self.wm, self.eh)
        self.notifier.start()


    def myAddWatch(self,towatch):

        self.wm.add_watch(towatch, mask, rec=True) 
            
    def myStopNotifier(self):
        self.notifier.stop()
        
    def convertGui(self,param):
        convertWorker = convert.GuiConvert(param)
        if convertWorker.convertGuiFile():
            print "Conversion successful. File that was convert: ", param
        else:
            print "Can`t convert file: ", param
            
class AppUi2Py():
    '''
    Main class. Create watcher thread.
    '''
    def __init__(self,params):
        '''
        Constructor
        '''    
        self.toWatch = params
        self.watcher = MyWatcher()
        self.watcher.myAddWatch(self.toWatch)
        while True:
            try:             
                self.watcher.notifier.process_events()
                if self.watcher.notifier.check_events():
                    self.watcher.notifier.read_events()
                
                pass
            except KeyboardInterrupt:
                self.watcher.myStopNotifier()
                break

def Help():
    '''
    Display the help text and example
    '''
    print __doc__

    
def Main(argv):
    
    try:
        opts, args = getopt.getopt(argv,"hi:",["help","input="])
    except getopt.GetoptError:
        Help()
        sys.exit(1) 
    if opts != []:
        for opt,arg in opts:
            if opt in ('-h','--help'):
                Help()
                sys.exit()
            elif opt in ('-i','--input'):
                AppUi2Py(arg)  
    else:
        print Help()

    sources = ''.join(args)  # @UnusedVariable

