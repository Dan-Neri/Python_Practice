"""You are given two integer arrays nums1 and nums2, sorted in non-decreasing 
order, and two integers m and n, representing the number of elements in nums1 
and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be 
stored inside the array nums1. To accommodate this, nums1 has a length of 
m + n, where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length 
of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6] 
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming 
from nums1.

Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to
ensure the merge result can fit in nums1.



Constraints:

    nums1.length == m + n
    nums2.length == n
    0 <= m, n <= 200
    1 <= m + n <= 200
    -109 <= nums1[i], nums2[j] <= 109

 

Follow up: Can you come up with an algorithm that runs in O(m + n) time?
"""

#Strategy: keep track of a pointer for each array. Then run from the back,
#Largest to smallest numbers and insert into the empty space at the end of 
#nums1

#time complexity: O(n) to O(m + n)
#space complexity: O(1)

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        indexA = m - 1
        indexB = n - 1
        if nums1:
            numA = nums1[indexA]
        if nums2:
            numB = nums2[indexB]
        for i in range(m + n):
            if indexA < 0 and indexB >= 0:
                nums1[-(i + 1)] = numB
                indexB -= 1
                if indexB >= 0:
                    numB = nums2[indexB]
            elif indexB < 0 and indexA >= 0:
                #nums2 is empty and the rest of nums1 is already sorted correctly
                break
            elif indexA >= 0 and numA >= numB:
                nums1[-(i + 1)] = numA
                indexA -= 1
                if indexA >= 0:
                    numA = nums1[indexA]
            elif indexB >= 0 and numB >= numA:
                nums1[-(i + 1)] = numB
                indexB -= 1
                if indexB >= 0:
                    numB = nums2[indexB]
            else:
                print("error")

