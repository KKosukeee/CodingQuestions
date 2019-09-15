"""
Solution for Value equal to index value
https://practice.geeksforgeeks.org/problems/value-equal-to-index-value/0
"""

# code
def solve(array):
    """
    Given an array of positive integers. Your task is to find that element whose value is equal to that of its index value.

    Input:
    The first line of input contains an integer T denoting the number of test cases.
    The first line of each test case is N, size of array. The second line of each test case contains array elements.

    Output:
    Print the element whose value is equal to index value. Print "Not Found" when index value does not match with value.
    Note: There can be more than one element in the array which have same value as their index. You need to print every such element's index separated by a single space. Follows 1-based indexing of the array.

    Constraints:
    1 ≤ T ≤ 30
    1 ≤ N ≤ 50
    1 ≤ A[i] ≤ 1000

    Example:
    Input:
    2
    5
    15 2 45 12 7
    1
    1

    Output:
    2
    1

    ** For More Input/Output Examples Use 'Expected Output' option **

    Args:
        array(list[int]):

    Returns:
        None:

    """
    result = []
    for i in range(len(array)):
        if i + 1 == array[i]:
            result.append(str(i + 1))
    print(' '.join(result) if result else 'Not Found')


num_test = int(input())
for _ in range(num_test):
    length = int(input())
    array = list(map(int, input().split()))
    solve(array)

#            *
# [-2,-1,0,1,4]
# [ 0, 1,2,3,4]
# []