# Sorting 
Sorting is a set of algorithms that helps to arrange the data in specific order.
Now, arranging the data can be generally of two types, like ascending or descending, which is good for any int, float, char arrays or lists but actually we can also sort objects based on a specific criteria. This directory will introduce different sorting algorithms that can be applied over any datasets by just modifying the criteria. 

## Importance of Sorting Algorithms 
In real-world projects, we manage massive datasets where extracting meaningful insights(info) is critical. Finding specific data is significantly faster and more efficient when the dataset is organized by any criteria. Sorting algorithms are essential tools for this optimization. These algorithms are evaluated based on their Time and Space Complexity, as well as their Stability and Adaptability to different data structures.

### Exchange Sort (bubble sort)
This is the most common and naive sorting technique that just compares a pair of right data and swaps it on necessity. The common form of this sort, which is considred as a naive algorithm, is the bubble sort.
It's not very efficient because the worst-case of this technique requires O(n^2) time.
However, it takes O(1) as the auxillary space complexity bcoz there is noe additional space required!

### Selection Sort (staright selection & heap sort)
Selection Sort is an intelligent sorting algorithm wherein, the min or the max element is selected from the list and swapped with another misplaced element. There are genrally two types of selection sorts, Straight Selection Sort and the other one is Heap Sort.