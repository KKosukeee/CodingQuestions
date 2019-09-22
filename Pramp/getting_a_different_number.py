"""
Solution for Getting a Different Number
https://www.pramp.com/challenge/aK6V5GVZ9MSPqvG1vwQp
"""

def simple_linear_solution(arr):
    """
    Simple yet optimal solution that runs in O(N) in time, O(N) in space

    Args:
        arr(list[int]):

    Returns:
        int:

    """
    hash_table = set(arr)
    minimum = 0

    while minimum in hash_table:
        minimum += 1

    return minimum


def optimal_linear_solution(arr):
    """
    Optimal solution that runs O(n) in time and O(1) in space

    Args:
        arr(list[int]):

    Returns:
        int:

    """
    for i in range(len(arr)):
        temp = arr[i]
        while temp < len(arr) and arr[temp] != temp:
            arr[temp], arr[i] = arr[i], arr[temp]
            temp = arr[i]
    for i in range(len(arr)):
        if arr[i] != i:
            return i
    return len(arr)


def get_different_number(arr):
    """
    Given an array arr of unique nonnegative integers, implement a function getDifferentNumber that finds the smallest nonnegative integer that is NOT in the array.

    Even if your programming language of choice doesn’t have that restriction (like Python), assume that the maximum value an integer can have is MAX_INT = 2^31-1. So, for instance, the operation MAX_INT + 1 would be undefined in our case.

    Your algorithm should be efficient, both from a time and a space complexity perspectives.

    Solve first for the case when you’re NOT allowed to modify the input arr. If successful and still have time, see if you can come up with an algorithm with an improved space complexity when modifying arr is allowed. Do so without trading off the time complexity.

    Analyze the time and space complexities of your algorithm.

    Example:

    input:  arr = [0, 1, 2, 3]

    output: 4
    Constraints:

    [time limit] 5000ms

    [input] array.integer arr

    1 ≤ arr.length ≤ MAX_INT
    0 ≤ arr[i] ≤ MAX_INT for every i, 0 ≤ i < MAX_INT
    [output] integer

    Args:
        arr(list[int]):

    Returns:
        int:

    """
    return optimal_linear_solution(arr)


print(get_different_number([4, 1, 5, 0]))

# [0, 1, 2, 3]
# [0, 1, 2, 3]

# [0, 3, 1, 2]
# 1: [0, 2, 1, 3]
# 2: [0, 1, 2, 3]

# [0, 4, 1, 2]
# 1: [0, 1, 2, 4]
# 2: [0, 4, 1, 2]

# [0,5,4,1,3,6,2]
# 1: [0,1,2,3,4,5,6]
# 2: