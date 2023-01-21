"""

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the
characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false

"""

# My solution runtime Time complexity O(nm), n = length s, m = length t

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # initialize the 2d table
        m = len(t)
        n = len(s)
        T = [[0 for x in range(m)] for y in range(n)]

        # base case
        if n == 0:
            return True
        if m == 0:
            return False

        for i in range(0, n):
            for j in range(0, m):
                if s[i] == t[j]:
                    T[i][j] = 1 + T[i - 1][j - 1]
                else:
                    T[i][j] = max(T[i - 1][j], T[i][j - 1])

        if T[n - 1][m - 1] == n:
            return True
        return False