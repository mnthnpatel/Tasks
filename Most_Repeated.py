a = 0
data = [1,2,4,6,3,7,9,0,3,6,88,6]
number = data[0]
for element in data:
    b = (data.count(element))
    if b > a:
        a = b
        number = element  
print(f"{number} is most repeated number...")  



