class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money<children:
            return -1

        lea=money-children
        num=0
        for i in range(children):
            if  lea<7:
                break
            elif lea==10 and i==children-2:
                break
            elif i==children-1 and lea>7:
                break
            else:
                lea-=7
                num+=1
        return num
money=13
children=3
print(Solution().distMoney(money,children))
            
            
            
