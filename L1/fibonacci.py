el1 = 1
el2 = 1
t = 0;
print(el1)
print(el2)
while True:
  el3 = el1+el2
  el1 = el2+el3
  el2 = el3+el1
  print(el3)
  print(el1)
  print(el2)
  t += 1;
  if t > 20:
    break