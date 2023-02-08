#For Loops
#Print each fruit in a fruit list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)



#Looping Through a String
#Loop through the letters in the word "banana"
for x in "banana":
  print(x)



#The break Statement
#Exit the loop when x is "banana"
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break



#Exit the loop when x is "banana", but this time the break comes before the print
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)



#continue Statement
#Do not print banana
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)



#The range() Function
#Using the range() function
for x in range(6):
  print(x)

#Using the start parameter
for x in range(2, 6):
  print(x)

#Increment the sequence with 3 (default is 1)
for x in range(2, 30, 3):
  print(x)



#Else in For Loop
#Print all numbers from 0 to 5, and print a message when the loop has ended
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#Break the loop when x is 3, and see what happens with the else block
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")



#Nested Loops
#Print each adjective for every fruit
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)



#The pass Statement
for x in [0, 1, 2]:
  pass



#************EXERCISE************
#Loop through the items in the fruits list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)