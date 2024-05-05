class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf]*(amount+1)
        dp[0] = 0

        for a in range(1,amount+1):
            for c in coins:
                if c<=a:
                    dp[a] = min(dp[a],1+dp[a-c])

        return dp[-1] if dp[-1]!=math.inf else -1
