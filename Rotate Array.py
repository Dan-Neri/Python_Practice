"""
Given an integer array nums, rotate the array to the right by k steps, where k 
is non-negative.

 
Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

 

Constraints:

    1 <= nums.length <= 105
    -231 <= nums[i] <= 231 - 1
    0 <= k <= 105

 

Follow up:

    Try to come up with as many solutions as you can. There are at least three 
    different ways to solve this problem.
    Could you do it in-place with O(1) extra space?
"""

class Solution:
    #Strategy:Nested for statements. Outer one loops k times. Inner one loops
        #over the length of nums shifting each number to the right one index

    #Time complextiy: O(kN)
    #Space complexity: O(1)
    def rotate(self, nums: list[int], k: int) -> None:
        for i in range(k):
            currentNum = nums[-1]
            for j in range(len(nums)):
                if j < len(nums)-1:
                    nextNum = nums[j]
                nums[j] = currentNum
                currentNum = nextNum
        return nums
            
    #Strategy:Create a second array to store the rotation. Iterate through nums
        #copying each element to the index + kth element of the new array.

    #Time complextiy: O(N)
    #Space complexity: O(N)
    def rotateCopy(self, nums: list[int], k: int) -> None:
        rNums = nums[:]
        for i in range(len(nums)):
            rIndex = i + k
            while rIndex >= len(nums):
                rIndex -= len(nums)
            nums[rIndex] = rNums[i]
        return nums
        
    #Strategy:Start by placing the first number in the correct spot and storing
        #the number that is already there in a temp variable. Then place the 
        #new number in the correct spot and refresh the tmep variable. 
        #After n = len(nums) steps we will be done unless len(nums) is 
        #divisible by k. So each time you reach the end of nums we'll need to
        #increment the index by 1 or we'll just loop through the same indices

    #Time complextiy: O(N)
    #Space complexity: O(1)
    def rotateTrace(self, nums: list[int], k: int) -> None:
        offset = 0
        currentIndex = 0
        temp = nums[0]
        for i in range(len(nums)):
            currentNum = temp
            currentIndex += k
            while currentIndex >= len(nums):
                currentIndex -= len(nums)
            temp = nums[currentIndex]
            nums[currentIndex] = currentNum
            if (currentIndex == offset) and (i < len(nums)-1):
                currentIndex += 1
                temp = nums[currentIndex]
                offset += 1
        return nums
        
test = Solution()
print(test.rotate([1,2,3,4,5,6,7],3))