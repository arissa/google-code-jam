def store_credit(credit, items):
	for i in range(len(items) - 1):
		for j in range(i+1, len(items)):
			if items[i] + items[j] == credit:
				return(i+1, j+1)
	return "None"
# print(store_credit(100, [5,75,25]))
# print(store_credit(200, [150,24,79,50,88,345,3]))
# print(store_credit(8, [2,1,9,4,4,56,90,3]))