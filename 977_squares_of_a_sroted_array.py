"""
977. Squares of a Sorted Array
Easy
7.3K
183
Companies
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.



Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

"""

# time complexity analysis - nums.sort() = O(nlogn), while loop is linear O(n), O(nlogn) dominates

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            temp = nums[left]
            temp2 = nums[right]
            nums[left] = temp ** 2
            nums[right] = temp2 ** 2
            left += 1
            right -= 1
        nums.sort()
        return nums