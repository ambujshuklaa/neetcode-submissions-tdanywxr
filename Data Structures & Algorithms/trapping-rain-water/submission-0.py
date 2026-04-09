class Solution:
    def trap(self, height: List[int]) -> int:

        lMax=[]
        rMax=[]
        maxl=0
        maxr=0

        for i in range (0, len(height),1):
            if height[i] > maxl:
                lMax.append(height[i])
                maxl=height[i]
            else:
                lMax.append(maxl)
        
        for j in range(len(height)-1,-1,-1):
            if height[j] > maxr:
                rMax.append(height[j])
                maxr=height[j]
            else:
                rMax.append(maxr)
        rMax=rMax[::-1]

        print(lMax)                
        print(rMax) 

        res=0
        for i in range (0, len(height),1):
            if min(lMax[i],rMax[i]) - height[i] > 0:
                res = res + min(lMax[i],rMax[i]) - height[i]

        print(res)

        return res


        