class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        elif n==1:
            return True
        if n%4!=0:
            return False
        else:
            n=n//4
            return Solution().isPowerOfFour(n)
            
print(Solution().isPowerOfFour(13))
