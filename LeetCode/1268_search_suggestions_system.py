"""
Solution for 1268. Search Suggestions System
https://leetcode.com/problems/search-suggestions-system/
"""
from collections import defaultdict
import bisect
from typing import List

class Solution:
  """
  Runtime: 172 ms, faster than 33.33% of Python3 online submissions for Search Suggestions System.
  Memory Usage: 17.6 MB, less than 100.00% of Python3 online submissions for Search Suggestions System.
  """
  def initial_solution(self, products: List[str], searchWord: str) -> List[
    List[str]]:
    """
    An initial solution that runs in O(MN+KMlog(M)) in time where M = len(products),
    N = len(max(products[i])), K = len(searchWord)

    Args:
      products:
      searchWord:

    Returns:

    """
    trie = defaultdict(list)
    for product in products:
      prefix = ''
      for char in product:
        trie[prefix + char].append(product)
        prefix += char
    result = []
    prefix = ''
    for char in searchWord:
      result.append(sorted(trie[prefix + char])[:3])
      prefix += char
    return result

  def second_solution(self, products: List[str], searchWord: str) -> List[
    List[str]]:
    """
    The second solution that runs in O(MNlog(M)+KM) in time

    Args:
      products:
      searchWord:

    Returns:

    """
    trie = defaultdict(list)
    for product in products:
      prefix = ''
      for char in product:
        bisect.insort(trie[prefix + char], product)
        prefix += char
    result = []
    prefix = ''
    for char in searchWord:
      result.append(trie[prefix + char][:3])
      prefix += char
    return result

  def third_solution(self, products: List[str], searchWord: str) -> List[
    List[str]]:
    """
    The third solution that runs in O(MlogM+KMN)

    Args:
      products:
      searchWord:

    Returns:

    """
    products.sort()
    result = []
    for i in range(len(searchWord)):
      result.append(
        list(filter(lambda x: x.startswith(searchWord[:i + 1]), products))[:3])
    return result

  def suggestedProducts(self, products: List[str], searchWord: str) -> List[
    List[str]]:
    """
    Given an array of strings products and a string searchWord. We want to design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

    Return list of lists of the suggested products after each character of searchWord is typed.



    Example 1:

    Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
    Output: [
    ["mobile","moneypot","monitor"],
    ["mobile","moneypot","monitor"],
    ["mouse","mousepad"],
    ["mouse","mousepad"],
    ["mouse","mousepad"]
    ]
    Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
    After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
    After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
    Example 2:

    Input: products = ["havana"], searchWord = "havana"
    Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
    Example 3:

    Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
    Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
    Example 4:

    Input: products = ["havana"], searchWord = "tatiana"
    Output: [[],[],[],[],[],[],[]]


    Constraints:

    1 <= products.length <= 1000
    1 <= Σ products[i].length <= 2 * 10^4
    All characters of products[i] are lower-case English letters.
    1 <= searchWord.length <= 1000
    All characters of searchWord are lower-case English letters.

    Args:
      products:
      searchWord:

    Returns:

    """
    return self.third_solution(products, searchWord)

  """
  TRIE solution

  """