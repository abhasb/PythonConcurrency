""" 
Semaphores as a key synchronizaiton privimites in Python threading.
Understand how atomic counter manage thread access, prevent missed signals, and coordinate complex tasks like signaling between threads.

------------------------------------------------------------------------------------------------------------------------------

A semaphore is just an atomic counter that gets decremented by 1 whenever acquire() is invoked and incremented by one 
whenever release is called. 

The semaphore can be initialized with an initial count value. 
If none is specified, the semaphore is initialized with the value of 1.


acquire() :
If a thread invokes acquire() on a semaphore, the semaphore counter is decremented by one.
If the count is greater than 0, then the thread immediately returns from the acquire() call. 
If the semaphore counter is zero when a thread invokes acquire(), the thread gets blocked till another thread releases the semaphore.

relesae() :
When a thread invokes the release() method, the internal semaphore counter is incremented by one.
If the counter value is zero and another thread is already blocked on an acquire() then a release would unblock the waiting thread.
If multiple threads are blocked on the semaphore, then one thread is arbitrarily chosen.


Semaphores can be used in versatile ways. 
The primary use of semaphores is signaling among threads which are working to achieve a common goal. 
"""