# I: An array of integers
# O: a sorted array of the largest three integers
# C: Cant sort array, O(n) time | O(1) Space
# E: N/A 

# General idea: we can init an array with 3 -Infinity values, and iterate through the array and then just update these three index's.

def findThreeLargestNumbers(array):
	solution = [float('-inf'), float('-inf'), float('-inf')]
	for num in array:
		if num > solution[2]:
			solution[0], solution[1], solution[2] = solution[1], solution[2], num
		elif num > solution[1]:
			solution[0], solution[1] = solution[1], num
		elif num > solution[0]:
			solution[0] = num
	return solution
