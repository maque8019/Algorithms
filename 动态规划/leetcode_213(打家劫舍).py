class Solution:
    def rob(self, nums):
        fir=0
        n=len(nums)
        if n==1:
            return nums[0]
        num2=nums[1:]
        m=len(num2)
        dp1=[0]*n
        dp1[1]=nums[0]
        dp2=[0]*n
        dp2[1]=num2[0]
        for i in range(2,m+1):  
            dp1[i]=max(dp1[i-2]+nums[i-1],dp1[i-1])
        for j in range(2,n):
            dp2[j]=max(dp2[j-2]+num2[j-1],dp2[j-1])
        return max(dp1[n-1],dp2[n-1])
nums=[2,3,2]
print(Solution().rob(nums))
            
