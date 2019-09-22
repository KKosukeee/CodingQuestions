"""
Solution for Array of Array Products
https://www.pramp.com/challenge/7Lg1WA1nZqfoWgPbgM0M
"""

# Brute force approach. Time: O(n^2), Space: O(n)
def naive_approach(arr):
    """
    Args:
        arr: list of integers to calculate array of array products

    Returns:
        list<int>: list of integers
    """
    if len(arr) == 1:
        return []

    result = []
    # outer loop
    for i in range(len(arr)):

        prod = 1
        # inner loop
        for j in range(len(arr)):
            if i != j:
                prod *= arr[j]

        result.append(prod)

    return result


def array_of_array_products(arr):
    """
    Given an array of integers arr, you’re asked to calculate for each index i the product of all
    integers except the integer at that index (i.e. except arr[i]). Implement a function
    arrayOfArrayProducts that takes an array of integers and returns an array of the products.


    Solve without using division and analyze your solution’s time and space complexities.

    Examples:

    input:  arr = [8, 10, 2]
    output: [20, 16, 80] # by calculating: [10*2, 8*2, 8*10]

    input:  arr = [2, 7, 3, 4]
    output: [84, 24, 56, 42] # by calculating: [7*3*4, 2*3*4, 2*7*4, 2*7*3]

    Args:
        arr: list of integers to calculate array of array products

    Returns:
        list<int>: list of integers
    """
    n = len(arr)
    if n == 0 or n == 1:
        return []

    prods = [1] * len(arr)
    prod = 1

    for i in range(len(arr)):
        prods[i] = prod
        prod *= arr[i]

    prod = 1
    for i in range(len(arr) - 1, -1, -1):
        prods[i] *= prod
        prod *= arr[i]

    return prods
