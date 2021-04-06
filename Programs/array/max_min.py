li = []
size = int(input("Enter the size of a list: "))
print("\nEnter the elements: \n")
for i in range(0, size):
	ele = int(input())
	li.append(ele)
m = li[0]
mi = li[0]
for i in range(0, size):
	if(li[i]>m):
		m = li[i]
	if(li[i]<mi):
		mi = li[i]
print("The maximum ele in list is: ", m)
print("the minimum ele in list is: ", mi)