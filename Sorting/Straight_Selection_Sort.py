# Straight Selection Sort

from array import array
# E.g. [5, 4, 6, 0, 2] -> [0, 4, 6, 5, 2] -> [0, 2, 6, 5, 4] -> [0, 2, 4, 5, 6]
def straight_selection_sort(array: int):
    for i in range(len(array)):
        min_index = i
        for j in range(i, len(array)):
            if (array[j] < array[min_index]):
                min_index = j # the inner loop checks the smallest and set it to min_index pointer
        array[i], array[min_index] = array[min_index], array[i] # here the swapping(sorting) happens
        return array



elements: int = int(input("Enter the no.of elements you want to push on the array: "))
arr: array = array('i', [])
for ele in range(0, elements):
    element: int = int(input(f"Enter {ele + 1} element: "))
    arr.append(element)
print(f"The original array is {arr}.")

sorted_array = straight_selection_sort(arr)
print(f"Sorted array is {sorted_array}.")