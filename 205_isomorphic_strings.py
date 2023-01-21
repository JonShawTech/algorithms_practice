"""

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.



Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false

"""

# my solution runtime O(n) linear

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        S = {}
        T = {}
        x = True
        for i in range(len(s)):
            if s[i] in S and S[s[i]] != t[i]:
                x = False
            if t[i] in T and T[t[i]] != s[i]:
                x = False
            S[s[i]] = t[i]
            T[t[i]] = s[i]

        return x