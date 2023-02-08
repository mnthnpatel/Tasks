#Print all key names in the dictionary, one by one
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)



#Print all values in the dictionary, one by one:
for x in thisdict:
  print(thisdict[x])



#You can also use the values() method to return values of a dictionary:
for x in thisdict.values():
  print(x)



#You can use the keys() method to return the keys of a dictionary
for x in thisdict.keys():
  print(x)



#Loop through both keys and values, by using the items() method
for x, y in thisdict.items():
  print(x, y)




#**********Copy a Dict************#
##Make a copy of a dictionary with the copy() method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)



#Make a copy of a dictionary with the dict() function
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)
