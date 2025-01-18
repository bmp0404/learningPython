import math
import sys
import random as rdm # rdm is alias
from enum import Enum
import lesson14_rps7

print(math.pi)
rdm.choice("123")


print(dir(rdm)) # dir shows what is inside module

for item in dir(rdm):
    print(item)

print(__name__) # shows name of module
print(math.__name__) # prints name

# can have methods in module that run when module is imported

lesson14_rps7.rock_paper_scissors()