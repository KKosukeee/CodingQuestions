"""
Solution for Quick Sort
https://practice.geeksforgeeks.org/problems/quick-sort/1
"""

# User function Template for python3
def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

def partition(arr, low, high):
    # add code here
    i = low
    p = arr[high]
    for j in range(low, high):
        if arr[j] < p:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

#         *
# [10,40,30]
# [10,30,40]
#         *
# [40,10,30]
