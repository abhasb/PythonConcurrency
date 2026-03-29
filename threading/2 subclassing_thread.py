""" 
How to create Python thread by subclassing the Thread class.
Understand the process of overriding the run method and constructor, and how to properly initialize the thread for effective multithreading.
"""

from threading import Thread
from threading import current_thread

class MyTask(Thread):
    
    def __init__(self):
        Thread.__init__(self, name="subclassThread", args=(2, 3))
        
    def run(self):
        print("{0} is executing".format(current_thread().name))
        
myTask = MyTask()

myTask.start()  # start the thread

myTask.join()  # wait for the thread to complete

print("{0} exiting".format(current_thread().name))
        
""" 
Important caveats to remember when subclassing the Thread class are:
    - we can only override the run() method and the constructor of the Thread class.
    - Thread.__init__() must be invoked if the subclass choses to override the constructor.
    - Note that the args or kwargs don't get passed to the run method.
"""