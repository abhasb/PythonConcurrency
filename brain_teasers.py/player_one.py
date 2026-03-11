class Player:
    # Number of players in the Game 
    count = 0
    def __init__(self, name): 
        self.name = name
        self.count += 1 
p1 = Player('Parzival')
print(Player.count)


""" 
Guess the output ?
Output : 0

Python attribute lookup Process. How instance and class dictionaries interact.

Every Python object stores it's attribute in a dict called __dict__. Python will first try to find attribute in the
instance dictionary, then in the instance's class dictionary __class__, and then up the instance hierarchy __mro__.

Finally, if the attribute we're are looking for is not found, Python will raise Attribute Error.

What happens when we try self.count += 1?

If we try self.count += 1 in the teaser, Python will translate it to self.count = self.count + 1. This means it'll
use getattr(self, count) and get the count defined in the Player class with the value of 0. Once Python has the value
of self.count + 1 = 1 on the right-hand side of the assignment (=), it'll call setattr(self, count, 1). The setattr
function will create a new entry in self.__dict__ that will shadow the count in Player. After that, we can print the Player.count, which is still 0. 
If we print p1.count, we'll get 1.


"""