import random

numAns = random.randint(1, 10)
while True:
  numG = input("Enter a number from one to ten ")
  if int(numG) > numAns:
    print("Too high!")
  if int(numG) < numAns:
    print("Too low!")
  if int(numG) == numAns:
    print("You are correct! The number is", numAns)
    break
input("Press enter/return to exit")

