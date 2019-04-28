"""
Solution for 4. Median of Two Sorted Arrays
https://leetcode.com/problems/median-of-two-sorted-arrays/
"""

class Solution:
    """
    Runtime: 76 ms, faster than 74.87% of Python3 online submissions for Median of Two Sorted
        Arrays.
    Memory Usage: 13.5 MB, less than 5.11% of Python3 online submissions for Median of Two Sorted
        Arrays.
    """
    # Space complexity: O(n + m)
    # Time complexity:  O(n + m)
    def findMedianSortedArrays(self, nums1, nums2):
        """
        There are two sorted arrays nums1 and nums2 of size m and n respectively.

        Find the median of the two sorted arrays. The overall run time complexity should be
        O(log (m+n)).

        You may assume nums1 and nums2 cannot be both empty.

        Example 1:

        nums1 = [1, 3]
        nums2 = [2]

        The median is 2.0
        Example 2:

        nums1 = [1, 2]
        nums2 = [3, 4]

        The median is (2 + 3)/2 = 2.5
        Args:
            nums1:
            nums2:

        Returns:

        """
        # --- Merge sort the array ---

        # Initialize new array
        new_array = []

        # Add both length to loop through
        length_of_two = len(nums1) + len(nums2)

        # Initialize index for both nums1 and nums2
        i, j = 0, 0

        # Loop through length of len(nums1) + len(nums2)
        while len(new_array) < length_of_two:
            # If i < len(nums1), then append nums2[j] and break
            if not i < len(nums1):
                new_array.append(nums2[j])
                j += 1
                continue

            # If j < len(nums2), then append nums1[i] and break
            if not j < len(nums2):
                new_array.append(nums1[i])
                i += 1
                continue

            # If nums1[i] < nums2[j], then add 1 to i
            if nums1[i] <= nums2[j]:
                new_array.append(float(nums1[i]))
                i += 1

            # Otherwise, add 1 to j
            else:
                new_array.append(float(nums2[j]))
                j += 1

        # --- End merge sort the array ---

        # --- Then find the median ---

        # If len(new_array) is divisible, then take mean of middle two items
        if len(new_array) % 2 == 0:

            # Take floor and slice two items from the index
            start_index = len(new_array) // 2 - 1

            # Take mean and return
            return sum(new_array[start_index:start_index + 2]) / 2.

        # Oterwise, return middle value
        else:
            index = len(new_array) // 2
            return new_array[index]

        # --- End then find the median ---
