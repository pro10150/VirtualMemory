from random import randint

capacity = input("Input capacity: ")
processList = []

# List of current pages in Main Memory
s = []

pageFaults = 0
# pageHits = 0

for i in range(10):
    rand = randint(0, 7)
    x = s.count(rand)
    processList.insert(i,rand)

print(processList)

for i in processList:

 # If i is not present in currentPages list
 if i not in s:

  # Check if the list can hold equal pages
  if(len(s) == int (capacity)):
   s.remove(s[0])
   s.append(i)
   print(s)

  else:
   s.append(i)
   print(s)

  # Increment Page faults
  pageFaults +=1

 # If page is already there in
 # currentPages i.e in Main
 else:

  # Remove previous index of current page
  s.remove(i)

  # Now append it, at last index
  s.append(i)
  print(s)


