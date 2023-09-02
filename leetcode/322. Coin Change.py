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

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        df = [amount+1] * (amount + 1)
        index = 1
        df[0] = 0

        while index <= amount:
            for c in coins:
                res = index - c
                if res>=0:
                    df[index] = min(df[res]+1,df[index])
            index += 1
        return df[amount] if df[amount] != (amount+1) else -1


