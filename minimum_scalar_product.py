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