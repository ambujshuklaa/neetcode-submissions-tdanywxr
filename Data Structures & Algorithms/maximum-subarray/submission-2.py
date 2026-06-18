class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l=[]
        for i in range(len(nums)):
            sum_value = nums[i]
            max_value= nums[i]
            for j in range(i+1, len(nums),1):
                # print(sum_value, nums[j])
                sum_value= sum_value + nums[j]
                max_value=max(sum_value,max_value)
            l.append(max_value)
        
        print(l)

        return max(l)
            











        