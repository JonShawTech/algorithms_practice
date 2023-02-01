"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.


Constraints:

0 <= n <= 30
"""

# Time complexity analysis - O(n) 

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = [0] * int(n + 1)

        # base case
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        f[0] = 0
        f[1] = 1

        for i in range(2, n + 1):
            f[i] = f[i - 1] + f[i - 2]

        return f[n]
