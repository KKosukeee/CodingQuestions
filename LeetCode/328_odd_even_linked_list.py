"""
Solution for 328. Odd Even Linked List
https://leetcode.com/problems/odd-even-linked-list/
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
  """
  Runtime: 32 ms, faster than 98.93% of Python3 online submissions for Odd Even Linked List.
  Memory Usage: 14.4 MB, less than 100.00% of Python3 online submissions for Odd Even Linked List.
  """
  def oddEvenList(self, head: ListNode) -> ListNode:
    """
    Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

    You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

    Example 1:

    Input: 1->2->3->4->5->NULL
    Output: 1->3->5->2->4->NULL
    Example 2:

    Input: 2->1->3->5->6->4->7->NULL
    Output: 2->3->6->7->1->5->4->NULL
    Note:

    The relative order inside both the even and odd groups should remain as it was in the input.
    The first node is considered odd, the second node even and so on ...

    Args:
      head:

    Returns:

    """
    if not head or not head.next:
      return head

    odd, even = head, head.next
    dummy = ListNode(0)
    dummy.next = head
    i, current = 3, head.next.next
    even_dummy = ListNode(0)
    even_dummy.next = even

    while current:
      if i % 2 != 0:
        odd.next = current
        odd = current
      else:
        even.next = current
        even = current
      current = current.next
      i += 1
    even.next = None
    odd.next = even_dummy.next
    return dummy.next