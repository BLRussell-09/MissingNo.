from random import randint

def find_missing_no(lst):
  for i in range(101):
    if i not in lst:
      print (i)

a = []
for i in range(101): #Generates a list of integers from 0 - 100
  a.append(i)
a.pop(a[a.index(randint(0,100))]) # Removes a random int from the list
find_missing_no(a)
