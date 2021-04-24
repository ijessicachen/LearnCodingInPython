#NOTE: please make an actual file with this name
#WRITE
f = open("filename.txt", "w") #a instead of w will append it at the end. w will override everything
f.write("hello!")
f.close()

#READ
f = open("filename.txt", "r")
content = f.read()
print(content)



#Sort() method
leaders = [
  "ABB, 90.00",
  "ROTo, 100.00",
  "BBOty, 112.20"
]
print(leaders)
#alphabetically
leaders.sort()
print(leaders)
#reverse alphabetically
leaders.sort(reverse = True)
print(leaders)

def length(item):
  return len(item)
#Sort by length (shrotest to longest)
leaders.sort(key=length)
print(leaders)

def extract_score(item):
  player = item.split(",")
  return float(player[1])
leaders.sort(key=extract_score)
print(leaders)
