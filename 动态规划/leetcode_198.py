class Solution:
    def rob(self,nums):
        n=len(nums)
        dp=[0]*(n+1)
        dp[0]=0
        dp[1]=nums[0]
        for i in range(2,n+1):
            dp[i]=max(dp[i-1],nums[i-1]+dp[i-2])
        return dp[n]
#nums=[1,2,3,1]
nums=[2,7,9,3,1]
print(Solution().rob(nums))
        
