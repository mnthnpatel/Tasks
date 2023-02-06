# Slicing...

b = "Hello, World!"
print(b[:5])
print(b[2:])
print(b[-5:-2])


# Upper Case...
a = "Hello, World!"
print(a.upper())

# Lower Case...
a = "Hello, World!"
print(a.lower())

# Remove Whitespace...
a = "   Hello, World! "
print(a.strip())


# Replace String....
a = "Hello, World!"
print(a.replace("H", "J"))


# Split String...
a = "Hello World Wide"
print(a.split())


# String Concatenation...

a = "Hello"
b = "World"
c = a + b
d = a + " " + b # To Add Space Between Them...
print(c)
print(d)


# String Format

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# Escape Character...

txt = "We are the so-called \"Vikings\" from the north."
print(txt)