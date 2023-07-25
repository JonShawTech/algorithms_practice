"""

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0

"""

# Time complexity analysis - O(Wn) W = amount, n = |coins| (pseudo polynomial)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        C = [float("inf")] * int(amount+1)
        C[0] = 0
        
        if amount == 0:
            return 0
                
        for j in range(len(coins)):
            for i in range(amount+1):
                if coins[j] <= i:
                    C[i] = min(C[i], 1+C[i - coins[j]])
             
                    
        if C[amount] == float("inf"):
            
            return -1
        else:
            return C[amount]
