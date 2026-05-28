class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        arr= [0]*(len(cost)+1)

        for i in range(len(cost)+1):
            if (i>1):
                arr[i]= min((arr[i-2] + cost[i-2]), (arr[i-1] + cost[i-1]))

        print(arr,arr[-1])

        return arr[-1]