""" 
How to create threads in python using the Thread class from threading module. 
Learn to pass arguments to threads, manage daemon threads, and control thread execution flow by starting and joining threads.
Understand the role of main thread in python's threading module.




Thread Constructor #

Thread(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)

The group argument is reserved for future extensions.
target is the code that the thread being created will execute. It can be any callable object.
A callable object can be a function or an object of a class that has a __call__ method.
We can pass arguments to the target either as a tuple args or a dictionary of key value pairs using kwargs.
The constructor takes a boolean specifying if the thread being created should be treated as a daemon thread.

"""

from threading import Thread
from threading import current_thread

def thread_task(a, b, c, key1, key2):
    
    print("{0} received the arguments: {1} {2} {3} {4} {5}".format(current_thread().name, a, b, c, key1, key2))
    
myThread = Thread(group=None,  # reserved
                  target=thread_task,  # callable object
                  name="demoThread",  # name of thread
                  args=(1, 2, 3),  # arguments passed to the target
                  kwargs={'key1': 777, 'key2': 111},  # dictionary of keyword arguments
                  daemon=None  # set true to make the thread a daemon
                  )

myThread.start()  # start the thread

myThread.join()  # wait for the thread to complete


""" 
Main Thread:

There has to another thread that is actually executing the code we wrote to create a new thread. 
This ab initio thread is called main thread.
The main thread is the thread from which the Python interpreter was started.


* Try to watch the treads by running in debugger mode.
"""
