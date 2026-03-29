"""
Understand daemon threads and how they differ from regualar threads.
How to create daemon threads, their role in program termination and key considertations when using them in concurrency.
Insights on managing background processes effectively in Python applications.

------------------------------------------------------------------------------------------------------------------------------

In computer science realm a daemon is a computer program that runs as a background process rather than being under control
of an interactive user.

A daemon thread in Python runs in the background.

The difference between a regular thread and a daemon thread is that a Python program will not exit until all regular/user threads terminate. 

However, a program may exit if the daemon thread is still not finished.


daemonThread = Thread(target=daemon_thread_task, daemon=True)
"""

from threading import Thread
from threading import current_thread
import time

def daemon_thread_task():
    while True:
        print("{0} executing".format(current_thread().name))
        time.sleep(1)

regularThread = Thread(target=daemon_thread_task, name="daemonThread", daemon=True)
regularThread.start()  # start the daemon thread

time.sleep(3)

print("Main thread exiting and Python program too")

""" 
In the above snippet the main thread creates a non-daemonic thread and exits.
However the program continues to run.

Daemon thread are shutdown abruptly.
Resources such as open files and database connections may not shut-down properly and daemon threads are not a good choice for such tasks.
One final caveat to remember is that if you don't specify the daemon parameter in the constructor then the daemonic property is inherited from the current thread.
"""