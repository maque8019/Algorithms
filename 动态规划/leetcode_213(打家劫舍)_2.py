class Solution:
    def rob(self, nums):
        if len(nums)==1:
            return nums[0]
        def myrob(num):
            a,b=0,num[0]
            n=len(num)
            if n==1:
                return b
            for i in range(2,n+1):
                a,b=b,max(a+num[i-1],b)
            return b
        return max(myrob(nums[1:]),myrob(nums[:len(nums)-1]))
nums=[2,7,9,3,1]
print(Solution().rob(nums))
