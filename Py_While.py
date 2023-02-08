#While Loops
#Print i as long as i is less than 6
i = 1
while i < 6:
  print(i)
  i += 1



#The break Statement
#Exit the loop when i is 3
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1



#continue Stateme
#Continue to the next iteration if i is 3
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)



#else Statement
#Print a message once the condition is false
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")



#************EXERCISE*************#
#Print i as long as i is less than 6
i = 1
while i < 6:
    print(i)
    i += 1