f2 = open("output.txt", "w")

with open("data.txt", "r") as myfile:
	data = myfile.readlines()

data_2 = data[::-1]

f2.writelines(data_2)

f2.close()


with open('data.txt') as f,  open('output.txt', 'w') as f2:
    f2.writelines(reversed(f.readlines()))