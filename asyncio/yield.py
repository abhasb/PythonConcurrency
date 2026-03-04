""" 
Explore the use of Yield keyword in Python to create generator functions that produces values on demand.
How yeild suspends a function's state allowing efficient generation of sequences without computing all
values upfront.

Normal return functions
def keep_learning_asynchronous():
    return "Yield"
    
Generator function using yield
def keep_learning_asynchronous():
    yield "Educative"
    
The return value of the generator function is a generator object that can be iterated over to retrieve the yielded values one at a time.

In order for the generator object to produce or yield us the string we invoke next on it.

Since we can pass generators into next we can think of them as iterators.
We can use them inside for loops as well.

We can also have multiple yield statements in a function.

If we attempt to invoke next() on a generator object that had already produced (yielded) all its values, we'll be thrown a StopIteration exception. 


Can we use yield and return statemetn both inside the same function ? 
Yes----
** 
If we invoke next() a second time we will receive a StopIteration exception. 
The second string will be passed in as the value to StopIteration exception. 
**




"""

def keep_learning_synchronous():
    yield "LoL"
    
    
def keep_learning_asynchronous():
    yield "LoL"
    return "End of generator function"


if __name__ == "__main__":
    str = keep_learning_synchronous()
    print(str)
    
    gen = keep_learning_synchronous()
    str = next(gen)
    print(str)
    
    
    gen = keep_learning_synchronous()
    for str in gen:
        print(str)
        
    
    