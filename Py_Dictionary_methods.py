#Methods
#Accessing Keys:
#get the value of "model" key without get method
thisdict1={
    "brand":"Ford",
    "model":"Mustang",
    "year":"1964"
}
x=thisdict1["model"]
print(x)


#get the value of "model" key with .get method
x=thisdict1.get("model")
print(x)
#diff btwn with and without get() is...with get() if there is no such key then it gives o/p as "none"....while without get() it will show an error that invalid key


#*******get keys**********#
x=thisdict1.keys()
print(x)


#*******get values*********#
x=thisdict1.values()
print(x)


#*******get itemes*****
x=thisdict1.items()
print(x)



#add items and check it will reflact the original dict
thisdict1={
    "brand":"Ford",
    "model":"Mustang",
    "year":"1964"
}
x=thisdict1.keys()
y=thisdict1.values()
z=thisdict1.items()
print(x)
print(y)
print(z)
thisdict1["color"]="white"       #add key value pair in dict
print(x)
print(y)
print(z)



#change value and check it will reflact the original dict
thisdict1={
    "brand":"Ford",
    "model":"Mustang",
    "year":"1964"
}
x=thisdict1.keys()
y=thisdict1.values()
z=thisdict1.items()
print(x)
print(y)
print(z)
thisdict1["year"]="2020"
print(x)
print(y)
print(z)



#check if key is represented or not
thisdict1={
    "brand":"Ford",
    "model":"Mustang",
    "year":"1964"
}
if "model" in thisdict1:
    print("Yes, 'model' is one of the keys in the thisdict1 dictionary")



#update year of the car by using update() method
thisdict1={
    "brand":"Ford",
    "model":"Mustang",
    "year":"1964"
}
x=thisdict1.update({"year":"2020"})
print(thisdict1)

