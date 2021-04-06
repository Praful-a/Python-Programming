row = int(input("Enter the row no. for mat: "))
col = int(input("Enter the column no. for mat: "))
mat1 = []
mat2 = []
mat3 = []
print("\nEnter the first matrix elements: \n")
for i in range(row):
	a = []
	for j in range(col):
		a.append(int(input()))
	mat1.append(a)

print("\nEnter the second matrix elements: \n")
for i in range(row):
	a = []
	for j in range(col):
		a.append(int(input()))
	mat2.append(a)
print("\nPrinting the first matrix: \n")
for i in range(row):
	for j in range(col):
		print(mat1[i][j], end=" ")
	print()
print("\nPrinting the second matrix: \n")
for i in range(row):
	for j in range(col):
		print(mat2[i][j], end=" ")
	print()

print('\nPrinting multiplication of two matrixes: \n')
for i in range(row):
	a = []
	for j in range(col):
		a.append(0)
	mat3.append(a)

for i in range(row):
	for j in range(col):
		for k in range(col):
			mat3[i][j] += mat1[i][k] * mat2[k][j]

for i in range(row):
	for j in range(col):
		print(mat3[i][j], end=" ")
	print()