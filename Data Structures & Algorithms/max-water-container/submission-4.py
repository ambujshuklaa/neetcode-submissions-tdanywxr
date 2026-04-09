class Solution:
    def maxArea(self, heights: List[int]) -> int:

        def calArea(a,b,h):
            l = abs(a-b)
            return l*h
        
        maxArea=0

        # for i in range(0,len(heights),1):
        #     j= len(heights)-1
        #     while(i<j):
                
        #         interimArea = calArea(i,j,min(heights[i],heights[j]))
                
        #         print(i,j,heights[i],heights[j],min(heights[i],heights[j]),interimArea)

        #         if interimArea > maxArea:
        #             maxArea=interimArea
        #         j= j - 1 

        # print(maxArea)

        i = 0
        j = len(heights) - 1

        while(i<j):

            interimArea = calArea(i,j,min(heights[i],heights[j]))
            
            print(i,j,heights[i],heights[j],abs(i-j),min(heights[i],heights[j]),interimArea)

            if interimArea > maxArea:
                maxArea=interimArea
            
            if heights[i] > heights[j]:
                j= j - 1

            elif heights[i] <= heights[j]:
                i= i+ 1

        return  maxArea  








