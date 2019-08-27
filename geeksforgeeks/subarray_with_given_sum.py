"""
Solution for Subarray with given sum
https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0

Given an unsorted array A of size N of non-negative integers, find a continuous sub-array which adds to a given number S.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. The first line of each test case is N and S, where N is the size of array and S is the sum. The second line of each test case contains N space separated integers denoting the array elements.

Output:
For each testcase, in a new line, print the starting and ending positions(1 indexing) of first such occuring subarray from the left if sum equals to subarray, else print -1.

Constraints:
1 <= T <= 100
1 <= N <= 107
1 <= Ai <= 1010

Example:
Input:
2
5 12
1 2 3 7 5
10 15
1 2 3 4 5 6 7 8 9 10
Output:
2 4
1 5

Explanation :
Testcase1: sum of elements from 2nd position to 4th position is 12
Testcase2: sum of elements from 1st position to 5th position is 15

** For More Input/Output Examples Use 'Expected Output' option **
"""

def max_sum_of_subarray_using_hash(array, n, sum):
    """
    A solution using hash map. This works with negative number as well.
    Runtime of this function is O(n) and the space is O(n) as well.
    Args:
        array(list[int]):
        n(int):
        sum(in):

    Returns:
        int:

    """
    hash_map = {sum: 0}
    cum_sum = 0
    for i, num in enumerate(array):
        cum_sum += num
        if cum_sum in hash_map:
            print(hash_map[cum_sum]+1, i+1)
            return 1
        else:
            hash_map[cum_sum+sum] = i+1
    print(-1)
    return 0

def max_sum_of_subarray_using_sliding_window(array, n, sum):
    """
    A solution using sliding window approach. This doesn't work with negative number.
    The runtime complexity is same as the previous algorithm
    Args:
        array(list[int]):
        n(int):
        sum(int):

    Returns:
        int:

    """
    i, j = 0, 1
    current_sum = array[i]
    while j <= len(array):
        if current_sum > sum and i < j-1:
            current_sum -= array[i]
            i += 1
        if current_sum == sum:
            print(i+1, j)
            return 1
        if j < len(array):
            current_sum += array[j]
        j += 1
    print(-1)
    return 0
