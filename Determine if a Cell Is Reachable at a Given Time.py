"""
You are given four integers sx, sy, fx, fy, and a non-negative integer t.

In an infinite 2D grid, you start at the cell (sx, sy). Each second, you
must move to any of its adjacent cells.

Return true if you can reach cell (fx, fy) after exactly t seconds, or 
false otherwise.

A cell's adjacent cells are the 8 cells around it that share at least 
one corner with it. You can visit the same cell several times.

 

Example 1:
     |     |     |     |     |     |     |
_____|_____|_____|_____|_____|_____|_____|_____
     |Start|*****|*****|*****|     |     |
_____|_____|_____|_____|_____|_____|_____|_____
     |     |     |     |     |*****|     |
_____|_____|_____|_____|_____|_____|_____|_____
     |     |     |     |     |*****|     |
_____|_____|_____|_____|_____|_____|_____|_____
     |     |     |     |     |     |Finish
_____|_____|_____|_____|_____|_____|_____|_____
     |     |     |     |     |     |     |
     |     |     |     |     |     |     |
Input: sx = 2, sy = 4, fx = 7, fy = 7, t = 6
Output: true
Explanation: Starting at cell (2, 4), we can reach cell (7, 7) in 
exactly 6 seconds by going through the cells depicted in the picture 
above. 

Example 2:
     |     |     |     |     |     |     |
_____|_____|_____|_____|_____|_____|_____|_____
     |Start|     |     |     |     |     |
_____|_____|_____|_____|_____|_____|_____|_____
     |     |*****|     |     |     |     |
_____|_____|_____|_____|_____|_____|_____|_____
     |     |     |*****|*****|Finish     |
_____|_____|_____|_____|_____|_____|_____|_____
     |     |     |     |     |     |     |
     |     |     |     |     |     |     |

Input: sx = 3, sy = 1, fx = 7, fy = 3, t = 3
Output: false
Explanation: Starting at cell (3, 1), it takes at least 4 seconds to 
reach cell (7, 3) by going through the cells depicted in the picture 
above. Hence, we cannot reach cell (7, 3) at the third second.

 

Constraints:

  - 1 <= sx, sy, fx, fy <= 109
  - 0 <= t <= 109
"""

class Solution:
    #Strategy: This question can be computed logically using a
      #mathematical function rather than programatically. The quickest
      #way to traverse the grid will be by moving diagonally. That will
      #get you one cell closer to the finish in both the horizontal and
      #vertical directions. Therefore, it will always take at least
      #max(abs(fx - sx), abs(fy - sy)) seconds to reach the end. It is
      #also trivial to reach the finish in any amount of seconds greater
      #than this by simply moving horizontally or vertically instead of 
      #diagonally, which would add one extra second, or by moving to any
      #space and then moving back to the previous space, which would
      #add two extra seconds. The only exception to this would be if the
      #starting cell and finishing cell are the same. In this case, the
      #minimum amount of time required to reach the finish is zero
      #seconds. However, since we must move at least one space each
      #second, it will take at least 2 seconds to move away from the
      #finish and then back to it. In this case, all values of t should
      #return True except for one.
      
        #1. Calculate the minimum amount of seconds required to reach
            #the finish, requiredTime, using the formula mentioned 
            #above.
        #2. Check if we are already at the finish.
        #3. If we are, return False if t = 1 otherwise return True
        #4. If we don't start at the finish, Return True if 
            #t >= requiredTime and False otherwise

    #Time complextiy: O(1)
    #Space complexity: O(1)
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, 
                          t: int) -> bool:
        requiredTime = max(abs(fx - sx), abs(fy - sy))
        if sx == fx and sy == fy:
            if t == 1:
                return False
            else:
                return True
        elif t >= requiredTime:
            return True
        else:
            return False
    
if __name__ == "__main__":
    test = Solution()
    print(test.isReachableAtTime(2,4,7,7,6))
    print(test.isReachableAtTime(3,1,7,3,3))