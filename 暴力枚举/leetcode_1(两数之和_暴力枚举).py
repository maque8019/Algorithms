class Solution:
    def twoSum(self, nums,target):
        inp=[]
        for idx,num in enumerate(nums):
            if idx!=len(nums):
                for idx1,num1 in enumerate(nums):
                    if num+num1==target and idx1>idx:
                        inp.append(idx)
                        inp.append(idx1)
        return inp
nums=[3,3]
target=6
print(Solution().twoSum(nums,target))
                    
            
        
