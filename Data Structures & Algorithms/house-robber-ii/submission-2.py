class Solution:
    def rob(self, nums: List[int]) -> int:

        def robb1(nums):
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
        
        if len(nums)==1:
            return nums[0]
            
        print(max(robb1(nums[:-1]), robb1(nums[1:])))

  

        return(max(robb1(nums[:-1]), robb1(nums[1:])))
        