# Bubble Sort

from array import array

def bubble_sort(array:int):
    for i in range(len(array) - 1):
        for ele in range(1, len(array)):
            if array[ele] < array[ele - 1]:
                array[ele - 1], array[ele] = array[ele], array[ele - 1]
    return array


elements: int = int(input("Enter the no.of elements you want to push on the array: "))
arr: array = array('i', [])
for ele in range(0, elements):
    element: int = int(input(f"Enter {ele + 1} element: "))
    arr.append(element)
print(f"The original array is {arr}.")

sorted_array = bubble_sort(arr)
print(f"Sorted array is {sorted_array}.")