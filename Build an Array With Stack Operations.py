"""
You are given an integer array target and an integer n.

You have an empty stack with the two following operations:

    - "Push": pushes an integer to the top of the stack.
    - "Pop": removes the integer on the top of the stack.

You also have a stream of the integers in the range [1, n].

Use the two stack operations to make the numbers in the stack (from the 
bottom to the top) equal to target. You should follow the following 
rules:

  - If the stream of the integers is not empty, pick the next integer 
    from the stream and push it to the top of the stack.
  - If the stack is not empty, pop the integer at the top of the stack.
  - If, at any moment, the elements in the stack (from the bottom to the
    top) are equal to target, do not read new integers from the stream 
    and do not do more operations on the stack.

Return the stack operations needed to build target following the 
mentioned rules. If there are multiple valid answers, return any of 
them.

 

Example 1:

Input: target = [1,3], n = 3
Output: ["Push","Push","Pop","Push"]
Explanation: Initially the stack s is empty. The last element is the top
of the stack.
Read 1 from the stream and push it to the stack. s = [1].
Read 2 from the stream and push it to the stack. s = [1,2].
Pop the integer on the top of the stack. s = [1].
Read 3 from the stream and push it to the stack. s = [1,3].

Example 2:

Input: target = [1,2,3], n = 3
Output: ["Push","Push","Push"]
Explanation: Initially the stack s is empty. The last element is the top of the stack.
Read 1 from the stream and push it to the stack. s = [1].
Read 2 from the stream and push it to the stack. s = [1,2].
Read 3 from the stream and push it to the stack. s = [1,2,3].

Example 3:

Input: target = [1,2], n = 4
Output: ["Push","Push"]
Explanation: Initially the stack s is empty. The last element is the top of the stack.
Read 1 from the stream and push it to the stack. s = [1].
Read 2 from the stream and push it to the stack. s = [1,2].
Since the stack (from the bottom to the top) is equal to target, we stop the stack operations.
The answers that read integer 3 from the stream are not accepted.

 

Constraints:

  - 1 <= target.length <= 100
  - 1 <= n <= 100
  - 1 <= target[i] <= n
  - target is strictly increasing.


"""

class Solution:
    #Strategy:
        #1. Iterate through the stream and push the next number onto the
            #stack
        #2. Check if the number is part of the target or not
        #3. If it is, move to the next number in the target
        #4. If it isn't, pop the last number from the stack
        #5. Check to see if the stack matches the target
        #6. Push the next number onto the stack

    #Time complextiy: O(n)
    #Space complexity: O(n)
    def buildArray(self, target: list[int], n: int) -> list[str]:
        nums = []
        output = []
        currentIndex = 0
        if target:
            for i in range(1, n+1):
                nums.append(i)
                output.append("Push")
                if i == target[currentIndex]:
                    currentIndex += 1
                else:
                    nums.pop()
                    output.append("Pop")
                if nums == target:
                    return output
        return []
        
if __name__ == "__main__":
    test = Solution()
    print(test.buildArray([1,3], 3))
    print(test.buildArray([1,2,3], 3))
    print(test.buildArray([1,2], 4))
    print(test.buildArray([1,4], 3))
    print(test.buildArray([], 3))
    print(test.buildArray([1,3], 0))
    print(test.buildArray([1,3,6,12,15,18], 20))