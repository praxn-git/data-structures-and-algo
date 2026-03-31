# Heap Sort

from array import array

def heap_sort(array: int):
    return array



elements: int = int(input("Enter the no.of elements you want to push on the array: "))
arr: array = array('i', [])
for ele in range(0, elements):
    element: int = int(input(f"Enter {ele + 1} element: "))
    arr.append(element)
print(f"The original array is {arr}.")

sorted_array = heap_sort(arr)
print(f"Sorted array is {sorted_array}.")