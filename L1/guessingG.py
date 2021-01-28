import random

numAns = random.random(1, 10)
numG = input("Enter a number from one to ten")
while numG != numAns:
  numG = input("Enter a number from one to ten")
  if numG > numAns:
    print("Too high!")
  if numG < numAns:
    print("Too low!")
print("You are correct! The number is" + numAns)


