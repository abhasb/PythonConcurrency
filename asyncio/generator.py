""" 
How Python generator functions simplify asynchronous programming by yielding values lazily.
Impoving memory and compute efficiency.

Understand generator lifecycle states and the use of methods such as next and close to control execution flow.

Functions containing the yield statement compiled as generators. These functions returns an
object that supports the iterator protocol methods. The generator object created by default
receives the __next__() method.

Also note, the snippet iter(gen) is gen returns True. 
Thereby, confirming that a generator function returns a generator object which is an iterator.

* Generator functions allow us to procrastinate computing expensive values. We only compute the next value when required. This makes generators memory and compute efficient. They refrain from saving long sequences in memory or doing all expensive computations upfront.
* Generators when suspended retain the code location, which is the last yield statement executed, and their entire local scope. This allows them to resume execution from where they left off.
* Generator objects are nothing more than iterators.
* Remember to make a distinction between a generator function and the associated generator object which are often used interchangeably. A generator function when invoked returns a generator object and next() is invoked on the generator object to run the code within the generator function.
"""

def keep_learning_asynchronous():
    yield "LoL"
    
if __name__ == "__main__":
    gen = keep_learning_asynchronous()
    print(iter(gen) is gen)

