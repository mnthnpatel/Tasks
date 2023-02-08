#Create Dictionary
thisdict1={
    "brand":"Ford",
    "model":"Mustang",
    "year":"1964"
}
print(thisdict1)



#print values of dict
print(("Values: "),thisdict1.values())     #*****dict1_value?
print(thisdict1["brand"])



#dict are changeable,add,remove,doesn't allow same key...it overwrites it
#any type of data type allowed
thisdict2={
    "items":"Car",
    "brand":"Ford",
    "model":"Mustang",
    "year":"1964",
    "year":1965,
    "electric":False,
    "colors":["red","white","blue"]
}
print(thisdict2)



#print no of items in the dict
print(len(thisdict1))
print(len(thisdict2))



#print data type of dict
print(type(thisdict1))
print(type(thisdict2))



#use dict() method to make directory
thisdict3=dict(name="John",age=36,country="Noway")
print(thisdict3)