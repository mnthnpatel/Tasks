n1 = int(input("Enter Number 1 :- "))
n2 = int(input("Enter Number 2 :- "))

for i in range(1,11):
    for j in range(n1,n2+1):
        print(f"{j:2} X {i:2} = {j*i:2}",end="|")
    print()