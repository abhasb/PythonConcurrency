""" 
How iterables and iterators work in python, focus on their methods and the iterator protocols. 
What are differences between iterables and iterators, and how they enable looping over data structures.

-----Iterable------
An Iterable is an object that can be looped over it's member element using a for loop. An iterator 
is capable of returning it's members one by one. 

The __getitem()__ can be invoked to return a member at a specified index.

Dictionaries, set and files are not indexable but are iterable. 

Python allows to create iterables that are infinite called generators.

In order to qualify as an iterable, an object must define one of the two methods:
1. __iter__()
2. __getitem__()


-------Iterator-----
Iterator is an object which can be used to sequentially access the element of an iterable object.
Iterator exposes the __next__() method .

An iterator must support the following methods:
1. __iter__()
2. __next__()

The iterator object reutrn itself for the __iter__() method .

When the end of the iterable object iteration is reached, __next__() throws a StopIteration exception. All this is called protocols.
"""

if __name__ == "__main__":
    listOfInts = list()
    listOfInts.append(1)
    listOfInts.append(2)
    listOfInts.append(3)
    
    # get iterator of list using __iter__() method
    it = listOfInts.__iter__()
    print("Iterator of listOfInts: ", str(it))
    
    # get member element of list using __getitem__()
    print("First element of listOfInts: ", listOfInts.__getitem__(2))
    
    # iterator returns itself when passed to the iter function
    print("it is iter(it) = " + str(it is iter(it)))
    
    # get another iterator for list using the built in iter() method
    it_another = iter(listOfInts)
    print("it_another = " + str(it_another))
    
    print("iteration using iterator in a for loop")
    # iterate using the iterator
    for element in it_another:
        print(element)

    print("iteration using iterable in a for loop")
    # iterate using the iterable
    for element in listOfInts:
        print(element)
        
        
"""
Each call to .__iter__() creates a new, independent iterator object. The two different memory addresses confirm this — it and it_another are two separate objects that both point into the same underlying listOfInts data, but they are distinct instances with their own internal state (specifically, their own position/index counter).

Think of it like two separate bookmarks in the same book — the book is the same, but each bookmark tracks a different reading position independently.

You can verify this:


it = listOfInts.__iter__()
it_another = listOfInts.__iter__()

next(it)        # advances only it → 1
next(it)        # advances only it → 2
next(it_another) # it_another is still at start → 1
This is why line 47 checks it is iter(it) — that returns True because an iterator returns itself from __iter__(), not a new object. But calling .__iter__() on the list (an iterable, not an iterator) always creates a fresh iterator.
"""