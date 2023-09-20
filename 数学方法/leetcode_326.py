import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        ls=[]
        for i in range(32):
            ls.append(i)
        if round(math.log(n)/math.log(3),13) in ls:
            return True
        else:
            return False
n=26
print(Solution().isPowerOfThree(n))
