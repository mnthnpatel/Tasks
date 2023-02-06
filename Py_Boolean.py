# Print a message based on whether the condition is True or False:
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


# Following Will Return True...
print(bool("Hello"))
print(bool(15))
print(bool(["apple", "cherry", "banana"]))


# Following Will Return False...
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))



# Print "YES!" if the function returns True, otherwise print "NO!":
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")


# Check if an object is an integer or not:
x = 200
print(isinstance(x, int))