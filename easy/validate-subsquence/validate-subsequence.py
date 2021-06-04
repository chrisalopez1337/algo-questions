# I: two non-empty arrays of ints
# O: a bool representing if array2 is a subsequence of array1
# C: O(n) time | O(1) space
# E: N/A

# General Idea: Iterate over A1 and whenever A1 matches A2, increment A2. 
# If A2 is iterated through then the answer is true : its false

def validate_subsequence(array, sequence):
    i, x = 0, 0
    while i < len(array) and x < len(sequence):
        if sequence[x] == array[i]:
            x += 1
        i += 1
    return x == len(sequence)

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
expected = True

print(validate_subsequence(array, sequence), expected)
