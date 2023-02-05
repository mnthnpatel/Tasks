# Append...
Sample = [21,23,354,57,89,9,67]
Sample.append(0)
print(Sample)

# Extend...
Even = [2,4,6]
Odd = [1,3,5]
Even.extend(Odd)
print(Even)

# Change List Items...
Languages = ["C++","Python","Swift","R","Rust","Java"]
Languages[0] = "C"
print(Languages)

# Length...
print(len(Languages))

# Del...
del Languages[1]
print(Languages)

# Remove...
Languages.remove("Java")
print(Languages)

# Check Element In List...
print("Swift" in Languages)
print("Leo" in Languages)

# List Comprehension
Numbers = [number*number for number in range(1,6)]
print(Numbers)

list1 = [5,3,2,6,12,10]

list1.sort()
print(list1)

list1.reverse()
print(list1)

list1.insert(3,4)
print(list1)

list1.pop(3)
print(list1)