# I: An array of integers
# O: A sorted array
# C: Must use Insertion Sort
# E: N/A

# General Idea: We init the first int as our sublist of sorting, and as we iterate through, we go back through that sub list and insert it where it belongs

array = [8, 5, 2, 9, 5, 6, 3]

def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j-1]:
            swap(j, j-1, array)
            j -= 1
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
