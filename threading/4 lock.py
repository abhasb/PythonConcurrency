""" 

Fundamentals of Python's lock object within the threading module.
How the acquire and release methods control access between threads, preventing race conditions and ensuring thread safe operations.
Demonstrate synchronization and explain common pitfalls like deadlocks.

------------------------------------------------------------------------------------------------------------------------------
Lock : 
Lock is primitive synchronizaiton construct available in Python. 
It offers two methods:
    (1) : acquire()
    (2) : release()
    
A lock object can be in only two states : Locked or Unlocked
A lock object can only be unlocked by a thread that locked it in first place.
A Lock object is equivalent of a mutex that you read about in operating systems theory.

Acquire :
Whenever a Lock object is created it is initialized with the unlocked state.
Any thread can invoke acquire() on the lock object to lock it.
Advanced readers should note that acquire() can only be invoked by a single thread at any point because the GIL ensures that only one thread is being executed by the interpreter.
This is in contrast to other programming languages with more robust threading models where multiple threads could be executing on different cores and theoretically attempt to acquire a lock at exactly the same time.
If a Lock object is already acquired/locked and a thread attempts to acquire() it, the thread will be blocked till the Lock object is released.
If the caller doesn't want to be blocked indefinitely, a floating point timeout value can be passed in to the acquire() method. The method returns true if the lock is successfully acquired and false if not.

Release:
The release() method will change the state of the Lock object to unlocked and give a chance to other waiting threads to acquire the lock.
"""

import time
from threading import Lock
from threading import Thread
from threading import current_thread

sharedState = [1, 2, 3]
my_lock = Lock()


def thread1_operations():
    my_lock.acquire()
    print("{0} has acquired the lock".format(current_thread().name))

    time.sleep(3)
    sharedState[0] = 777

    print("{0} about to release the lock".format(current_thread().name))
    my_lock.release()
    print("{0} released the lock".format(current_thread().name))


def thread2_operations():
    print("{0} is attempting to acquire the lock".format(current_thread().name))
    my_lock.acquire()
    print("{0} has acquired the lock".format(current_thread().name))

    print(sharedState[0])
    print("{0} about to release the lock".format(current_thread().name))
    my_lock.release()
    print("{0} released the lock".format(current_thread().name))

if __name__ == "__main__":
    # create and run the two threads
    thread1 = Thread(target=thread1_operations, name="thread1")
    thread1.start()

    thread2 = Thread(target=thread2_operations, name="thread2")
    thread2.start()

    # wait for the two threads to complete
    thread1.join()
    thread2.join()
    
""" 
Deadlock example:

Two threads are instantiated and each tries to invoke release() on the lock acquired by the other thread, resulting in a deadlock.
The below example demonstrates that a thread can't release a lock it has not locked. Furthermore, trying to release an unacquired lock will result in an exception.
"""

def thread_one(lock1, lock2):
    lock1.acquire()
    time.sleep(1)
    lock2.release()


def thread_two(lock1, lock2):
    lock2.acquire()
    time.sleep(1)
    lock1.release()