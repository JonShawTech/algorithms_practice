

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            print(mid)

            if nums[mid] == target:
                return nums.index(target)
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
