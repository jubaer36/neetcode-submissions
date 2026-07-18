class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [None] * (n+1)
        for i in range(min(n+1,4)):
            dp[i] = i
        for i in range(4,n+1):
            if dp[i] is None:
                dp[i] = dp[i-1] + dp[i-2]
            else:
                return dp[i]
        
        return dp[n]
        
        
        
        