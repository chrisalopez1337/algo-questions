# I: A nested array
# O: The product sum of all ints in that array
# C: O(n) Time | O(d) space where d is the greatest depth of special arrays 
# E: N/A

# The distance of a array is how far it is nested, 
# [x, y] = x + y
# [x, [y, z]] = x + 2 * (y + z)
# 1, 2, 3 
# and a single nested [x, [y, [z]]] = x + 2 * (y + 3z)

# So the general idea is to iterate through the array and get the sum of each
# sub array where it is the depth * the added value (depth starts at 1)

def productSum(array, level=1):
	sum = 0
	for item in array:
		if type(item) is list:
			sum += productSum(item, level+1)
		else:
			sum += item
	return sum * level
