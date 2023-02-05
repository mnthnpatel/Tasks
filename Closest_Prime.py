def big(n):
    while True:
        n = n+1
        for i in range(2,n):
            if(n%i==0):
                break
        else:
            return n
def small(n):
    while True:
        n = n-1
        for i in range(2,n):
            if(n%i==0):
                break
        else:
            return n

Num = int(input("Enter Value Of Num :- "))
print(f"{small(Num)} And {big(Num)} Are The Closest Prime Values Of {Num} .")