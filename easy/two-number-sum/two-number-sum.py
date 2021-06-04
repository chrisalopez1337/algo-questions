# I: An array of ints, and a target int
# O: An empty array if target is not contained, else an array containing the ints that = the target
# C: O(n) Time | O(n) Space
# E: N/A

# Basic Idea: We want to store the seen numbers into a dict and as we traverse
# the number required to solve is:
# s = (target - x) 
# if s is in the Dict we find our solution

def two_number_sum(array, target):
    seen = {}
    for x in array:
        solution = target - x
        if solution in seen:
            return [solution, x]
        seen[x] = x
    return []

# Sample test case
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
expected = [-1, 11]

print(two_number_sum(array, targetSum), expected)

