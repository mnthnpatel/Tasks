data = ["Hello  ","App   le","  Work","H elp"]
m = []
for i in range(0,len(data)):
    s = "".join(data[i].split())
    m.append(s)   
print(m)
