class Solution:
    def minCount(self, coins) -> int:
        minNum=0
        for i in coins:
            if i%2==0:
                minNum+=i/2
            else:
                minNum+=i//2+1
        return int(minNum)
coins=[1,1,1,1]
print(Solution().minCount(coins))
                
