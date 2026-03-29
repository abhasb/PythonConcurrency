""" 
How conditional varaibles enhance threading syncrhonizaiton in Python by enabling threads to wait for particular conditions.
Understand the limitation of lock and busy waiting, and discover efficient ways to coordinate threads in concurrency scenarios.

------------------------------------------------------------------------------------------------------------------------------

Synchronization mechanisms need more than just mutual exclusion. A general need is to be able to wait for another thread to do something.
Condition variables provide mutual exclusion and the ability for threads to wait for a predicate to become true.

Why we need condition variables ?

Locks are used to enforce serial access to shared data. However, locks aren't enough when threads needs to coordinate
among themselves.

Imagine a scenario where we have two threads working together to find prime numbers and print them. 
Say the first thread finds the prime number and the second thread is responsible for printing the found prime. 
The first thread (finder) sets a boolean flag whenever it determines an integer is a prime number. 
The second (printer) thread needs to know when the finder thread has hit upon a prime number. 
The naive approach is to have the printer thread do a busy wait and keep polling for the boolean value.
"""
from threading import Thread
import time


def printer_thread_func():
    global prime_holder
    global found_prime

    while not exit_prog:
        while not found_prime and not exit_prog:
            time.sleep(0.1)

        if not exit_prog:
            print(prime_holder)

            prime_holder = None
            found_prime = False


def is_prime(num):
    if num == 2 or num == 3:
        return True

    div = 2

    while div <= num / 2:
        if num % div == 0:
            return False
        div += 1

    return True


def finder_thread_func():
    global prime_holder
    global found_prime

    i = 1

    while not exit_prog:

        while not is_prime(i):
            i += 1

        prime_holder = i
        found_prime = True

        while found_prime and not exit_prog:
            time.sleep(0.1)

        i += 1


found_prime = False
prime_holder = None
exit_prog = False

printer_thread = Thread(target=printer_thread_func)
printer_thread.start()

finder_thread = Thread(target=finder_thread_func)
finder_thread.start()

# Let the threads run for 5 seconds
time.sleep(3)

# Let the threads exit
exit_prog = True

printer_thread.join()
finder_thread.join()
"""

One shortcoming of the above approach is we have the printer thread constantly polling in the while loop for found_prime
variable to become true. This is called busy waiting and is highly discouranged as it unnecessarily wastes CPU cycles.
Ideally the printer thread should go to sleep so that it doesn't consume system resources and be woken up when the
condition it needs to act upon becomes true. This can be achived through condition variables.
"""

""" 
How to use condition variables in Python's threading module to coordinate threads. 
Understand the correct idiomatic of wait and notify methods, handling locks properly, and preventine issues like spurious wakeups
by using loops for condition checks.

------------------------------------------------------------------------------------------------------------------------------

There are two important methods for conditon variables:
    - wait() : invoked to make thread sleep and give up resources.
    - notify() : invoked by a thread when a condition becomes true and the invoking threads wants to inform the waiting thread
                 or threads to proceed
                 
A condition variables is always associated with lock. The lock can be either reentrant or plain vanilla lock.
The associated lock must be acquired before a thread can invoke wait() or notify() on the conditon variable.

We can create a lock ourselves and pass it to condition variables constructor. If not lock object is passed
then the lock is created underneath the hood by the condition variable.


"""
from threading import Condition
cond_var = Condition()