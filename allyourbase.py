#in order to get min possible #of seconds, base is #of unique chars
#number cannot start with 0, so the first digit must be 1
#next unique digits are each assigned increasing values
#process: count num of unique chars
#then assign new symbols, first digit is 1, rest is increasing
#then convert to base 10
def min_seconds(string):
	translated_string= ""
	translations = {}
	translations[string[0]] = 1
	for char in string:
		if char != string[0]:
			translations[char] = 0
			break
	trans = 2
	for char in string:
		if char not in translations:
			translations[char] = trans
			trans+= 1 #this is not very robust, what about letters?
	for char in string:
		translated_string += str(translations[char])
	return to_base_ten(translated_string, len(translations))
def to_base_ten(string, base):
	answer = 0
	number = int(string)
	digit = 0
	while number:
		answer += (number%10)*(pow(base,digit))
		digit += 1
		number= number//10
	return answer

print(min_seconds("cats"))
print(min_seconds("zig"))
print(min_seconds("11001001"))