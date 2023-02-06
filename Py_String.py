# Assign String to a Variable
a = "Hello"
print(a)


# You can assign a multiline string to a variable by using three quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)



# Or three single quotes:

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)


# Get the character at position 1 (remember that the first character has the position 0):
a = "Hello, World!"
print(a[1])



# Loop through the letters in the word "banana":
for x in "banana":
  print(x,end=" ")
print()


# The len() function returns the length of a string:
a = "Hello,"
print(len(a))



# Check if "free" is present in the following text:
txt = "The best things in life are free!"
print("free" in txt) # Casse-Sesitive



# print only if "expensive" is NOT present:
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
