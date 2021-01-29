el1 = 1
el2 = 1
print(el1)
print(el2)
for t in range (0, 21):
  el3 = el1+el2
  el1 = el2+el3
  el2 = el3+el1
  print(el3)
  print(el1)
  print(el2)
#maybe change so it's only one number out every time the loop runs