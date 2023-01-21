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

# My solution rutime O(nm) n = length s, m = length t

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        T = [[0 for x in range(len(t))] for y in range(len(s))]

        if len(s) == 0:
            return True
        if len(t) == 0:
            return False

        for i in range(0, len(s)):
            for j in range(0, len(t)):
                if s[i] == t[j]:
                    T[i][j] = 1 + T[i - 1][j - 1]
                else:
                    T[i][j] = max(T[i - 1][j], T[i][j - 1])

        if T[len(s) - 1][len(t) - 1] == len(s):
            return True
        return False