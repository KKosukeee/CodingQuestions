"""
Solution for 1274. Number of Ships in a Rectangle
https://leetcode.com/problems/number-of-ships-in-a-rectangle/
"""


# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """

class Sea(object):
   def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
     pass
#
class Point(object):
  def __init__(self, x: int, y: int):
    self.x = x
    self.y = y

class Solution(object):
  """
  Runtime: 40 ms, faster than 87.54% of Python3 online submissions for Number of Ships in a Rectangle.
  Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Number of Ships in a Rectangle.
  """
  def countShips(self, sea: 'Sea', topRight: 'Point',
                 bottomLeft: 'Point') -> int:
    """
    (This problem is an interactive problem.)

    On the sea represented by a cartesian plane, each ship is located at an integer point, and each integer point may contain at most 1 ship.

    You have a function Sea.hasShips(topRight, bottomLeft) which takes two points as arguments and returns true if and only if there is at least one ship in the rectangle represented by the two points, including on the boundary.

    Given two points, which are the top right and bottom left corners of a rectangle, return the number of ships present in that rectangle.  It is guaranteed that there are at most 10 ships in that rectangle.

    Submissions making more than 400 calls to hasShips will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.



    Example :



    Input:
    ships = [[1,1],[2,2],[3,3],[5,5]], topRight = [4,4], bottomLeft = [0,0]
    Output: 3
    Explanation: From [0,0] to [4,4] we can count 3 ships within the range.


    Constraints:

    On the input ships is only given to initialize the map internally. You must solve this problem "blindfolded". In other words, you must find the answer using the given hasShips API, without knowing the ships position.
    0 <= bottomLeft[0] <= topRight[0] <= 1000
    0 <= bottomLeft[1] <= topRight[1] <= 1000

    Args:
      sea:
      topRight:
      bottomLeft:

    Returns:

    """
    total = 0
    if topRight.x >= bottomLeft.x and topRight.y >= bottomLeft.y and sea.hasShips(
        topRight, bottomLeft):
      if bottomLeft.x == topRight.x and bottomLeft.y == topRight.y: return 1
      my, mx = (topRight.y + bottomLeft.y) // 2, (
            topRight.x + bottomLeft.x) // 2
      total += self.countShips(sea, topRight, Point(mx + 1, my + 1))
      total += self.countShips(sea, Point(mx, topRight.y),
                               Point(bottomLeft.x, my + 1))
      total += self.countShips(sea, Point(mx, my), bottomLeft)
      total += self.countShips(sea, Point(topRight.x, my),
                               Point(mx + 1, bottomLeft.y))
    return total

  """
  Clarification 
  1. Are they sorted?

  Solution
  1. Call hasShips method for each quater
  2. If the method returns True, then divide the rectangle into four
  3. Count the number of ships in total
  """