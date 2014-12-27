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