from random import randint

def printArr(arr, n) :
	for i in range(n) :
		print(arr[i], end = " ")

def randomList(m, n):
	arr = [0] * m
	for i in range(n) :
		arr[randint(0, n) % m] += 1
	printArr(arr, m)



n = int(input("Enter Total Number :- "))
m = int(input("Enter Random Number :- "))
randomList(m, n)
