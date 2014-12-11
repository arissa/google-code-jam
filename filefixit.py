
def create_tree(given):
	paths = {}
	for path in given:
		folders = path.split("/")[1:]
		curr = paths
		for i in range(len(folders)):
			if folders[i] not in curr:
				curr[folders[i]] = {}
			curr = curr[folders[i]]
	return paths

def num_new(given_paths, new_path):
	folder_tree = create_tree(given_paths)
	new_path = new_path.split("/")[1:]
	count = 0
	curr = folder_tree
	for folder in new_path:
		if folder in curr:
			curr = curr[folder]
		else:
			count += 1
	return count
#TESTS
# ex1 = ["/a","/a/f","/c/e"]
# ex2 = ["/a/b/c/d/e","/b/z","/a/b/z/x"]
# print(num_new(ex1, "/b/d")) #2
# print(num_new(ex2, "/b/z")) #0
# print(num_new(ex2, "/a/b/f")) #1

