# b = input("Enter String :- ")
b = "Programming"
for i in range(len(b)):
    c = (b[i:])
    d = (" " * i)
    print(f"{d}{c} | {c[::-1]}")