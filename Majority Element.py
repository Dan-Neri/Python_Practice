"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than [n / 2] times. You 
may assume that the majority element always exists in the array.


Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

 

Constraints:

    n == nums.length
    1 <= n <= 5 * 104
    -109 <= nums[i] <= 109
    
Follow-up: Could you solve the problem in linear time and in O(1) space?
"""

#Strategy: create a dictionary to count the number of times each different
    #value appears in nums. Once any count reaches n/2 you can be certain it is
    #the majority element

#Time complextiy: O(N)
#Space complexity: O(N) number of distinct values in nums which could be at
    #most (n-1)/2

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count[num] > len(nums)/2:
                return num
                
#Strategy: Since there will be more of the majority element than all other 
    #values in nums combined, we can find it by counting like elements. Iterate
    #through nums and keep only a single running count starting at 0. If the 
    #count is 0, set the majority element to the current number and increment 
    #the count. Then every time you find the same number increment the count 
    #and decrement the count every time you find a different number.

#Time complextiy: O(N)
#Space complexity: O(1)
    
    def majorityElementBetter(self, nums: list[int]) -> int:
        count = 0 
        majElem = None
        for num in nums:
            if count == 0:
                majElem = num
                count += 1
            elif num == majElem:
                count += 1
            elif num != majElem:
                count -= 1
            else:
                print("error")
                break
        return majElem