#Python String Formatting
#String format()
#Add a placeholder where you want to display the price
price = 49
txt = "The price is {} dollars"
print(txt.format(price))


#Format the price to be displayed as a number with two decimals
txt = "The price is {:.2f} dollars"
print(txt.format(price))



#Multiple Values
quantity=3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))



#Index Numbers...a number inside the curly brackets {0}
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

#if you want to refer to the same value more than once, use the index number
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))



#Named Indexes
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))
