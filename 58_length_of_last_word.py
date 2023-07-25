"""

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

"""

# Time complexity analysis - O(n)

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0    
  
        for i in reversed(range(len(s))):
            if s[i] != ' ':
                count+=1
       
            if count > 0 and s[i] == ' ':
                break     
                       
            
        return count
            

    
