""" 
Fundamental's of Rlock in python, a reentrant lock that permits a thread to acquire it multiple times.
Understand it's ownership, recursion tracking, and how to properly acquire and release RLocks to avoid deadlocks in multithreaded programming.

------------------------------------------------------------------------------------------------------------------------------

A reentract lock is defined as a lock which can be acquired by the same thread.
A RLock object carries a notion of ownership.
If a thread acquires a RLock object, it can chose to reacquire it as many times as possible.

In contrast to Lock, the reentrant lock is acquired twice without blocking.
Note that it is imperative to release the lock as many times as it is locked.
Otherwise the lock remains in locked state and any other threads attempting to acquire the lock get blocked. 
"""

from threading import RLock
from threading import Thread


def child_task():
    rlock.acquire()
    print("child task executing")
    rlock.release()


rlock = RLock()

rlock.acquire()
rlock.acquire()

rlock.release()

# UNCOMMENT THE FOLLOWING LINE TO MAKE THE
# PROGRAM EXIT NORMALLY.
# rlock.release()

thread = Thread(target=child_task)
thread.start()
thread.join()