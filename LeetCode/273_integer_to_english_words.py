"""
Solution for 273. Integer to English Words
https://leetcode.com/problems/integer-to-english-words/
"""

class Solution:
  """
  Runtime: 32 ms, faster than 82.35% of Python3 online submissions for Integer to English Words.
  Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Integer to English Words.
  """
  def numberToWords(self, num):
    """
    Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

    Example 1:

    Input: 123
    Output: "One Hundred Twenty Three"
    Example 2:

    Input: 12345
    Output: "Twelve Thousand Three Hundred Forty Five"
    Example 3:

    Input: 1234567
    Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
    Example 4:

    Input: 1234567891
    Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

    Example 1:

    Input: 123
    Output: "One Hundred Twenty Three"
    Example 2:

    Input: 12345
    Output: "Twelve Thousand Three Hundred Forty Five"
    Example 3:

    Input: 1234567
    Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
    Example 4:

    Input: 1234567891
    Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"

    :type num: int
    :rtype: str
    """

    def read3digets(num):

      coding = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six',
                7: 'Seven', 8: 'Eight', 9: 'Nine', 0: 'Zero',
                10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen',
                14: 'Fourteen',
                15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen',
                19: 'Nineteen',
                20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty',
                60: 'Sixty', 70: 'Seventy',
                80: 'Eighty', 90: 'Ninety'}

      if num < 10:
        out = coding[num]
      elif num >= 10 and num < 20:
        out = coding[num]
      elif num >= 20 and num < 100:
        out = coding[num // 10 * 10]
        if num % 10 != 0:
          out = out + ' ' + coding[num % 10]
      elif num >= 100:
        out = coding[num // 100] + ' Hundred'
        if num % 100 != 0:
          out = out + ' ' + read3digets(num % 100)
      return out

    if num == 0:
      return 'Zero'
    groups = zip([1000000000, 1000000, 1000, 1],
                 [' Billion', ' Million', ' Thousand', ''])
    read = ''
    for n, unit in groups:
      val = num // n
      rem = num % n
      if val != 0:
        read = read + read3digets(val) + unit
        if rem == 0:
          break
        read = read + ' '
      num = rem
    return read