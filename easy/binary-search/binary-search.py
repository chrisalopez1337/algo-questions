# I: A sorted array of integers, and a target integer
# O: The index of the target int, or -1 if not located
# C: O(log(n)) Time | O(1) Space
# E: N/A

# General Idea: We want to do conquer and divide. We start at the middle of the array, check that value against the target and move to the right or left of the array dependant on if its < || > the target.

def binarySearch(array, target):
    right, left = len(array)-1, 0
    while left <= right:
        middle = (left + right) // 2
        if array[middle] == target:
            return middle
        elif array[middle] < target:
            left = middle + 1
        else:
            right = middle-1
    return -1

