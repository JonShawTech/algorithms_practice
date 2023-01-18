
"""
Prompt:
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

"""

# My solution time complexity O(n)

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum = [0] * int(len(nums))
        sum[0] = nums[0]

        if len(nums) == 1:
            return sum

        for i in range(1, len(nums)):
            sum[i] = nums[i] + sum[i - 1]
        return sum