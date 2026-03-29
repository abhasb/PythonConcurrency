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

-------------------------------------------------------------------------------------

ThreadPoolExecutor:

The ThreadPoolExecutor uses threads for executing submitted tasks.

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

* The submit calls return a future. The Future class represents the execution of the callable.
* Note that the invocation future.result() is blocking.

Generally this is not the pattern we use for submitting tasks. 
The idea is to be able to process multiple tasks in parallel and query the progress of the tasks using the future object.

* The map returns an iterator over the results of applying a function to a list of values.
* Both the function and the values are passed-in as parameters to the map() call.

executor = ThreadPoolExecutor(max_workers=10)
it = executor.map(square, (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
                     chunksize=1, timeout=2)
                     

-------------------------------------------------------------------------------------

ProcessPool Executor:

The process pool is very similar to a thread pool except that it is pool of processes that execute the task rather than threads.

from concurrent.futures import ProcessPoolExecutor
import multiprocessing
from multiprocessing import current_process
from threading import current_thread

import os


def say_hi(item):
    print(
        "\nhi " + str(item) + " executed in thread id " + current_thread().name + " in process id " + str(
            os.getpid()) + " with name " + current_process().name,
        flush=True)


if __name__ == '__main__':
    print("Main process id " + str(os.getpid()))
    multiprocessing.set_start_method('spawn')
    executor = ProcessPoolExecutor(max_workers=10)
    lst = list()
    for i in range(1, 10):
        lst.append(executor.submit(say_hi, "guest" + str(i)))

    for future in lst:
        future.result()

    executor.shutdown()
    
* Note that we can either have the processes spawned or forked by the process pool by setting the start method appropriately. 
* If you change the start method to fork on line#18 in the above example, the output would show that the processes were forked.


The only major difference when using map() with threads vs processes is the effect of the chunksize argument. 
In the above example, we have set the chunksize to one which implies each square will be calculated by a different process. 
If we change the chunksize to five then we only require two processes to square the ten input values. Depending on the usecase 
it may happen that a chunksize set to a higher value results in faster execution as time is saved in creating and then tearing
down more number of processes.
"""