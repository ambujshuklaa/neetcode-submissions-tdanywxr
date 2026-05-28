class Solution:
    def rob(self, nums: List[int]) -> int:

        arr=[0]*len(nums)

        for i in range(len(nums)):

            if i < 1:
                arr[i]=nums[i]
            
            else:
                arr[i]= max((arr[i-2] + nums[i]), arr[i-1])
        
        print(arr, arr[-1])

        if(len(arr)==2):
            return max(arr)

        return arr[-1]

        