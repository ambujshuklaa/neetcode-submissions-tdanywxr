class Solution:
    def climbStairs(self, n: int) -> int:
        a = [0]*n

        for i in range(n):
            if i ==0:
                a[i]=1
            elif i ==1:
                a[i]=2
            else:
                a[i]= a[i-1] + a[i-2]
        
        return a[len(a)-1]