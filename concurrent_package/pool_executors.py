""" 
Python's concurrent.futures module.
1. What are pool executors ? 
2. Understand how ThreadPoolExecutor and ProcessPoolExecutor facilitate parallel task execution with futures for efficient concurrency management. 
3. Learn how to use submit and map methods, handle blocking calls, manage thread and process pools, and handle task timeouts for practical concurrent programming.


"""

""" 
Pool executors :

To solve the management of the threads and processes Python provides concurrent.futures.
This package provides the Executor interface which can be used to submit tasks either to threads or processes.

The two subclasses are :
    1. ThreadPoolExecutor
    2. ProcessPoolExecutor
    
Tasks can be submitted synchronously or asynchronously to the pools for execution.





"""

from concurrent.futures import ThreadPoolExecutor
from threading import current_thread

def say_hi(item):

    print("\nhi " + str(item) + " executed in thread id " + current_thread().name, flush=True)
    
if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=10)
    lst = list()
    for i in range(1, 10):
        lst.append(executor.submit(say_hi, "guest" + str(i)))

    for future in lst:
        future.result()

    executor.shutdown()