

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