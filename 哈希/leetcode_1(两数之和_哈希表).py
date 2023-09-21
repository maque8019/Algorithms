class Solution:
    def twoSum(self, nums,target):
        hashtable=dict()
        for idx,num in enumerate(nums):
            if target-num in hashtable:
                return [hashtable[target-num],idx]

            hashtable[nums[idx]]=idx
target=8
nums=[1,2,3,4,5]
print(Solution().twoSum(nums,target))
            
