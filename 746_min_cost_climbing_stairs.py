"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.



Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
"""

# Time complexity analysis O(n)

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        T = [0] * n

        T[0] = cost[0]
        T[1] = cost[1]

        for i in range(2,n):
            T[i] = cost[i] + min(T[i-1], T[i-2])
        # print(T)

        return min(T[n-1],T[n-2])