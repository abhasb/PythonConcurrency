avengers = ['Bruce', 'Carol', 'Natasha', 'Tony']
idx = 3
avengers[idx], idx = 'Peter', 2  
print(avengers)


""" 
How Python handles multiple assignment and unpacking ? What is the evaluation order ?

It will first evaluate the right side of the = left to right. It will then evaluate the left side again from left to right.

In the line avengers[idx], idx = 'Peter', 2, Python first evaluates avengers[idx] = 'Peter'. Since idx is still third here, 
the fourth item on the list, Tony, is being replaced. Then Python will evaluate idx = 2.

Multiple assignments can be confusing and considered bad practice, so try to avoid this practice.
"""