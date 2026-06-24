class Solution:
    def jump(self, nums: List[int]) -> int:

        dist = [999] * (len(nums))
        
        dist[0]=0
        # print(dist)

        for i in range(len(nums)-1):
            for j in range(i+1, nums[i] + i + 1,1):
                if j < len(nums):
                    parent = dist[i]
                    # print('i coming from ',i,'going to j',j,'dist is ',parent,min(dist[j], parent + 1))
                    dist[j]=min(dist[j], parent + 1)
        
        print(dist)

        return dist[-1]

                
                


     