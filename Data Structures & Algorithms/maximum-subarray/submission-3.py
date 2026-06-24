class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l=[]
        # for i in range(len(nums)):
        #     sum_value = nums[i]
        #     max_value= nums[i]
        #     for j in range(i+1, len(nums),1):
        #         # print(sum_value, nums[j])
        #         sum_value= sum_value + nums[j]
        #         max_value=max(sum_value,max_value)
        #     l.append(max_value)
        
        # print(l)

        sum_max=0

        for i in range(len(nums)):
            if i ==0:
                sum_max=nums[i]
                l.append(sum_max)
            else:
                sum_max=max(sum_max + nums[i], nums[i])
                l.append(sum_max)

        print(l)

        return max(l)
            











        