def store_credit(credit, items):
	for i in range(len(items) - 1):
		for j in range(i+1, len(items)):
			if items[i] + items[j] == credit:
				return(i+1, j+1)
	return "None"
# print(store_credit(100, [5,75,25]))
# print(store_credit(200, [150,24,79,50,88,345,3]))
# print(store_credit(8, [2,1,9,4,4,56,90,3]))
import itertools
import sys
def min_scalar_product(v1, v2):
	min = sys.maxsize
	perms = itertools.permutations(v2)
	for p in perms:
		sum = 0
		for i in range(len(p)):
			sum += p[i]*v1[i]
		if sum < min:
			min = sum
	return min
# print(min_scalar_product([1,3,-5], [-2,4,1]))
# print(min_scalar_product([1,2,3,4,5], [1,0,1,0,1]))
# def alien_string_to_list(string):
# 	res = []
# 	for i in range(len(string)):
# 		if string[0] == "(":
# 			added = []
# 			pass


def alien(known_words, alien):
	count = 0
	for word in known_words:
		is_possible = True
		for i in range(len(word)):
			if word[i] not in alien[i]:
				is_possible = False
		if is_possible == True:
			count += 1
	return count


d = ["abc","bca", "dac", "dbc", "cba"]
print(alien(d, [["a","b"],["b","c"],["c","a"]])) #2
print(alien(d, [["a"], ["b"], ["c"]]))
print(alien(d,[["a","b","c"],["a","b","c"],["a","b","c"]]))
print(alien(d, [["x","y","z"], ["b"], ["c"]]))