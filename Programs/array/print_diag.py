n_rows = int(input("Number of rows: "))
n_columns = int(input("Number of columns: "))
matrix = []
print("Enter the entries row-wise")
for i in range(n_rows):
	a = []
	for j in range(n_columns):
		a.append(int(input()))
	matrix.append(a)
print("\nPrinting the 2-D matrix: \n")	
for i in range(n_rows):
	for j in range(n_columns):
		print(matrix[i][j], end=" ")
	print()

print("\nPrint the diagnal of 2-D matrix: ")
for i in range(n_rows):
	for j in range(n_columns):
		if(i == j):
			print(matrix[i][j], end=" ")
print()