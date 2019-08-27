"""
Solution for Count the triplets
https://practice.geeksforgeeks.org/problems/count-the-triplets/0
"""

def count_triplets(n, array):
    """
    Given an array of distinct integers. The task is to count all the triplets such that sum of two elements equals the third element.

    Input:
    The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. First line of each test case contains an Integer N denoting size of array and the second line contains N space separated elements.

    Output:
    For each test case, print the count of all triplets, in new line. If no such triplets can form, print "-1".

    Constraints:
    1 <= T <= 100
    3 <= N <= 105
    1 <= A[i] <= 106

    Example:
    Input:
    2
    4
    1 5 3 2
    3
    3 2 7
    Output:
    2
    -1

    Explanation:
    Testcase 1: There are 2 triplets: 1 + 2 = 3 and 3 +2 = 5

    ** For More Input/Output Examples Use 'Expected Output' option **
    Args:
        n(int):
        array(list[int]):

    Returns:
        int:

    """
    count = 0
    array.sort()
    k = len(array) - 1

    while k >= 2:
        i, j = 0, k - 1
        while i < j:
            temp = array[i] + array[j]
            if temp == array[k]:
                count += 1
            if temp <= array[k]:
                i += 1
            if temp >= array[k]:
                j -= 1
        k -= 1
    print(count if count > 0 else -1)
    return 1
