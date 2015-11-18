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

	for z in data:
		print(z)
		print(",")

if __name__ == '__main__':
    main(1500)
