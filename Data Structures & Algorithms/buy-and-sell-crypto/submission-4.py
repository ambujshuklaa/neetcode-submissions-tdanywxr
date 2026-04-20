class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # val = 0

        # pair = sorted([[p,s] for p,s in zip(prices,range(len(prices)))])

        # print(pair)

        # l=[]

        # for i in pair:
        #     l.append(i[1])
        
        # i=0
        # j=len(l)-1


        # while(i<j):
        #     if (l[j]-l[i] > 0) :
        #         break
        #     else:
        #         if (l[j] < l[i]) and l[j] != 0:
        #             # i = i + 1
        #             j = j-1
        #         elif l[j] == 0 : 
        #             j = j-1
        
        # print(l[i],l[j], prices[l[i]], prices[l[j]], prices[l[j]]- prices[l[i]])

        
        
        
        maxProfit = 0 
        i = 0 
        j = i + 1

        while (j<len(prices)): 
            if prices[j] > prices[i] :
                maxProfit = max(prices[j] - prices[i],maxProfit)
            else:
                i = j
            j = j + 1
        
        return maxProfit









        
        