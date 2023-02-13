import csv

file = open('data.xlsx','w')
file = csv.writer(file)
file.writerow(['Name','Language','E_Number'])

Row = int(input("How Many Records You Want To Insert ? :- "))
for i in range(Row):
    Name = input("Enter Name :- ")
    Lang = input("Enter Programming Language :- ")
    Enum = int(input("Enter Enrollment Number :- "))
    file.writerow([Name,Lang,Enum])
    print()

print("Data Inserted Successfully")