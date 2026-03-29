""" 
How to use Python's Event objects to synchronize threads effectively. 
Understand the internal boolean flag mechanism, learn to coordinate multiple thread.

------------------------------------------------------------------------------------------------------------------------------

An event object is one of the simplest primitives available for synchronization.
Internally, it has a boolean flag that can be set or unset using the methods set() and clear(). 
Additionally, a thread can check if the flag is set to true by invoking the is_set() method.

The event object exposes a wait() method that threads can invoke to wait for the internal boolean flag to become true.
If the flag is already true, the thread returns immediately.
If there are multiple threads waiting on the event object and an active thread sets the flag then all the waiting threads are unblocked.

Event is a convenience class and a wrapper over a condition variable with a boolean predicate.
This is the most common setup for many cooperating threads where two or more threads coordinate among themselves on a boolean predicate.


"""