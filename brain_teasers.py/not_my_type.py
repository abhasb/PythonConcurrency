def add(a: int, b: int) -> int: 
  return a + b

val = add('1', '2') 
print(val)

"""
Now back to our teaser. We add a and b, which are of type str. 
The + operator (defined by add) in str does concatenation. For example, it makes ‘a’ + ‘b’ → ‘ab’.
"""