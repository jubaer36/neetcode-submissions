class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [None] * (n+1)
        def helper(n):
            if dp[n] is not None:
                return dp[n]
            if n <= 3:
                dp[n] = n
                return dp[n]
        
            dp[n] = helper(n-1) + helper(n-2)
            return dp[n]
        return helper(n)
        
        
        
        