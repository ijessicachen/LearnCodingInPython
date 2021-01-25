# Load a module, a module is a package for a set of functions.
import random

#setup an index to track
index = 0

#the randint includes the start and stop values
#num = random.randint(0, 10)
while True:
  num = random.randint(0, 10)
  print("{0}: {1}".format(index, num))
  index += 1
  if(num == 10):
    break