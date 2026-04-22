class Solution:
    def search(self, nums: List[int], target: int) -> int:

        i = 0
        j = len(nums) - 1


        while(i<=j):
            print(i,j,int((i + j ) / 2))

            val = int((i + j ) / 2)

            if nums[val] == target:
                return val
            
            elif (i==j):
                return -1

            else:

                if target > nums[val]:
                    i = val + 1
                
                else:
                    j = val - 1
        
        return -1

        