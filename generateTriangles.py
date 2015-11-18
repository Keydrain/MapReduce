#!/usr/local/bin/python3

import random

def main(sizeOfArray):

	data = [[0 for x in range(sizeOfArray)] for x in range(sizeOfArray)]
	
	#print(data)
	a = 0
	for y in range(sizeOfArray):
		b = random.randint(0,sizeOfArray-1)
		c = random.randint(0,sizeOfArray-1)
		d = random.randint(0,sizeOfArray-1)

		data[a][b] = 1
		data[a][c] = 1
		data[b][a] = 1
		data[b][c] = 1
		data[c][a] = 1
		data[c][b] = 1
		data[d][a] = 1 #connect the data to come point
		data[a][d] = 1
		a = d

	for i in range(sizeOfArray):
		data[i][i] = 0
	
	print('[', end="")
	for z in range(len(data)):
		print(data[z], end="")
		if z != len(data)-1:
			print(",")
		else:
			print(']')

	return data

if __name__ == '__main__':
    main(15)
