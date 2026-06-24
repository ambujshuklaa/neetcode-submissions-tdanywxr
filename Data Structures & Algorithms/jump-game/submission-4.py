class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        visited=[0]* (len(nums))

        visited[0]=1

        for i in range(len(nums)-1):
            if visited[i]==1:
                for j in range(i+1,i + nums[i]+1,1):
                    if j < len(nums):
                        # print('starting from index i',i,'going to index j',j, nums[i])
                        visited[j]=1
        print(visited,visited[-1])

        if visited[-1]==1:
            return True
        else:
            return False

        




        