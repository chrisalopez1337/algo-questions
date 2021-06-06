# I: An array of ints
# O: a sorted array
# C: O(n^2) time | O(1) space
# E: N/A

def bubbleSort(array):
    swapped, i = False, 0
    while i < len(array)-1:
        if array[i] > array[i+1]:
            array[i], array[i+1], swapped = array[i+1], array[i], True
        i += 1
    if swapped == True:
        return bubbleSort(array)
    return array

