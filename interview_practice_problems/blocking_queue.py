""" 
Blocking Queue | Bounded Buffer | Consumer Producer

- Explore how the implement blocking queue using bounded buffer using Python.
- Learn synchronization between producer and consumer threads by managing enqueue and dequeue operations with condition variables to handle blocking and notification.
- Understand the importance of notifyAll in thread communication to avoid deadlocks.

"""

""" 
A blocking queue is defined as a queue which blocks the caller of the enque method if there's no more capacity to add the new item being enqueued..
Similarly, the queue blocks the dequeue caller if there are no items in the queue.

Also, the queue notifies a blocked enqueuing thread when space becomes available and a blocked dequeuing thread when an item becomes available in the queue.


The queue.Queue module already provides a synchronized queue out of the box. 
We'll be creating one from scratch that can be used by multiple consumers and producers.
"""


from threading import Condition

class BlockingQueue:
    
    def __init__(self, max_size: int):
        self.max_size = max_size
        self.cur_size = 0
        self.cond = Condition()
        self.q = []

    def enqueue(self, item):
        self.cond.acquire()
        while self.cur_size == self.max_size:
            self.cond.wait()

        self.q.append(item)
        self.curr_size += 1
        
        self.cond.notify_all()
        self.cond.release()
        
    def dequeue(self):
        self.cond.acquire()
        while self.cur_size == 0:
            self.cond.wait()
            
        item = self.q.pop(0)
        self.cur_size -= 1
        
        self.cond.notify_all()
        self.cond.release()
        
        return item
    
""" 
Does it matter if we use notify() or notify_all() method in our implementation?

Consider a situation with two producer threads and one consumer thread all working with a queue of size one.
It's possible that when an item is added to the queue by one of the producer threads, the other two threads are blocked waiting on the condition variable.
If the producer thread after adding an item invokes notify() it is possible that the other producer thread is chosen by the system to resume execution.
The woken up producer thread would find the queue full and go back to waiting on the condition variable, causing a deadlock.
Invoking notify_all() assures that the consumer thread also gets a chance to wake up and resume execution.
"""
        