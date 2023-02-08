#Python RegEx
#Import the re module
import re

#Search the string to see if it starts with "The" and ends with "Spain"
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(txt)



#The findall() Function
#Print a list of all matches
import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

#Return an empty list if no match was found
import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)



#search()
#Search for the first white-space character in the string
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

#Make a search that returns no match
import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)



#split()
#Split at each white-space character
import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

#Split the string only at the first occurrence
import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)



#sub()
#Replace every white-space character with the number 9
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

#Replace the first 2 occurrences
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)



#match object
#Do a search that will return a Match Object
import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object

#Print the position (start- and end-position) of the first match occurrence.
#The regular expression looks for any words that starts with an upper case "S"
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

#Print the string passed into the function
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

#Print the part of the string where there was a match.
#The regular expression looks for any words that starts with an upper case "S"
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())