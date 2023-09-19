class Solution:
    def myPow(self,x:float,n:int):
        if n<0:
            x=1/x
            n=abs(n)
        if n==1:
            return x
        elif n==0:
            return 1
        elif n==2:
            return x*x
        elif n==3:
            return x*x*x
        else:
            m=int(n**(1/2))
            m2=m**2
            d=n-m2
            a=Solution().myPow(x,d)
            x=Solution().myPow(x,m)
            return a*Solution().myPow(x,m)
print(Solution().myPow(2,-2))
        
