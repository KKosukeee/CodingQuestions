"""
Solution for Find The Duplicates question on Pramp
https://www.pramp.com/challenge/15oxrQx6LjtQj9JK9XlA
"""

# Time: O(n+m), Space: O(min(n,m))
def naive_approach(arr1, arr2):
    """
    Naive approach to find duplicates in arr1 and arr2
    Args:
        arr1: list containing integers to search duplicate with
        arr2: list containing integers to search duplicate with

    Returns:
        list: containing duplicate numbers in arr1 and arr2
    """
    duplicate = []
    i, j = 0, 0
    n, m = len(arr1), len(arr2)

    while i < n and j < m:
        # 2
        if arr1[i] == arr2[j]:
            duplicate.append(arr1[i])
            i += 1
            j += 1
        # 3
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1

    return duplicate

# Time: O(nlog(m)), Space: O(min(n,m))
def find_duplicates(arr1, arr2):
    """
    Optimal approach to find duplicates in arr1 and arr2 via binary search
    Args:
        arr1: list containing integers to search duplicate with
        arr2: list containing integers to search duplicate with

    Returns:
        list: containing duplicate numbers in arr1 and arr2
    """
    duplicate = []
    for x in arr1:
        if binary_search(arr2, x) == x:
            duplicate.append(x)

    return duplicate

def binary_search(arr, value):
    """
    Iterative binary search function
    Args:
        arr: list to look for a value
        value: integer value to search from arr

    Returns:
        int: returns value if found, otherwise -1
    """
    start = 0
    end = len(arr) - 1

    while start <= end:
        center = start + ((end - start) // 2)

        if arr[center] == value:
            return value
        elif arr[center] < value:
            start = center + 1
        else:
            end = center - 1

    return -1

arr1 = [1, 2, 3, 5, 6, 7]
arr2 = [3, 6, 7, 8, 20]
print(find_duplicates(arr1, arr2))
