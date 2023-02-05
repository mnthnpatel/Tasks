Company = {
    "CEC" : "Python",
    "Google" : "Java",
    "List" : ["C","C++",100],
    "Another" : {"Leo" : "IGL"}
}

print(Company["CEC"])
print(Company["Another"]["Leo"])

# Empty Dictionary
E = {}
print(type(E))

# Key...
print(Company.keys())

# Items...
print(Company.items())

# Values...
print(Company.values())

# Update...
Company2 = {"Bosch" : "Embedded C"}
Company.update(Company2)
print(Company)

# Get...
print(Company.get("Bosc"))
print(Company.get("Bosch"))

# Add Elements...
Company["City"] = "Ahmedabad"
print(Company)

# Change Element...
Company["Google"] = "Php"

# Del...
del Company["List"]
print(Company)