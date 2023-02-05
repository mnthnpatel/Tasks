Hex_Value = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A' , 'B', 'C', 'D', 'E', 'F']

Dec = int(input("Enter a Decimal Value :- "))
if Dec > 44613:
    print("Invalid")
    exit()
hexadecimal = ''


while(Dec>0):
    remainder = Dec%16
    hexadecimal = Hex_Value[remainder]+ hexadecimal
    Dec = Dec//16
    
print("Hexadecimal :- ",hexadecimal)