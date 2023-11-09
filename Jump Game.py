"""
You are given an integer array nums. You are initially positioned at the 
array's first index, and each element in the array represents your 
maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last 
index.

Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its 
maximum jump length is 0, which makes it impossible to reach the last 
index.

 

Constraints:

    1 <= nums.length <= 104
    0 <= nums[i] <= 105
"""

class Solution:
    #Strategy: select a number and then recurse through all possible 
    #iterations passing a slice of nums from the current index to the 
    #end

    #Time complextiy: 
    #Space complexity: 
    def canJump(self, nums: list[int]) -> bool:
        result = False
        if len(nums) == 1:
            return True
        if len(nums) == 0:
            return False
        if nums[0] == 0:
            return False
        for i in range(nums[0]):
            if self.canJump(nums[i+1:]):
                return True
        return result
        
test = Solution()
print(test.canJump([2,3,1,1,4]))
print(test.canJump([9,2,1,0,4]))
print(test.canJump([]))
print(test.canJump([1]))
print(test.canJump([5]))
print(test.canJump([0,2]))
print(test.canJump([2,1,9]))