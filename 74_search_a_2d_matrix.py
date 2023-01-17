

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # matrix = [[1,3,5,7],
        #          [10,11,16,20],
        #          [23,30,34,60]]

        for row in matrix:
            for element in row:
                if element == target:
                    return True
        return False