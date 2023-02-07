thislist = ["apple", "banana", "cherry"]
print(thislist)
print(type(thislist)) # Type Of List...
print(len(thislist)) # Length Of List...


# A list with strings, integers and boolean values:
list1 = ["abc", 34, True, 40, "male"]


# Accesesing List Items...

thislist = ["apple", "banana", "cherry"]
print(thislist[1])
print(thislist[-1])
print(thislist[2:5])



# Check if "apple" is present in the list:

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")



# Changing The Items Of List...

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)


# Insert "watermelon" as the third item:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)


# Using the append() method to append an item:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


# Add the elements of tropical to thislist:

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


# Remove "banana":

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


# Remove the second item:

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)


# Clear the list content:

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)



