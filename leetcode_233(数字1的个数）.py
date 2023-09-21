class Solution:
    def countDigitOne(self, n: int) -> int:
        st=str(n)
        n=len(st)
        dp=[]
        dp1=[]
        num=0
        strat=0
        for t in range(n):
            strat=9*strat+10**t+t
            dp1.append(strat)     
        for i in st:
            dp.append(int(i))
        dp.reverse()
        ax=dp[0]
        for idx,j in enumerate(dp):
            if idx==0 and j>=1:
                num+=1
            elif j==0:
                num+=0
            elif j>1 :
                num+=dp1[idx]-(10-j)*dp1[idx-1]  
            else :
                num+=dp1[idx]-(9-j)*dp1[idx-1]-(10-ax)*10**(idx-1)
            ax=j
        return num
n=100
print(Solution().countDigitOne(n))
                
            
        
