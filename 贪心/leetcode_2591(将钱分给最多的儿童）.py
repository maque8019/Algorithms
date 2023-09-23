class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money<children:
            return -1
        money=money-children
        cnt=min(money//7,children)
        money=money-7*cnt
        chil=children-cnt
        if money>0 and chil==0:
            cnt-=1
        elif money==3 and chil==1:
            cnt-=1
        else:
            cnt=cnt
        return cnt
            
        
        
