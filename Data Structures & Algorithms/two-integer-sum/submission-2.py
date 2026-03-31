class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        key_dict={}
        k=0

        for i in range (0,len(nums),1):
            for j in range (i+1,len(nums),1):
                if nums[i] + nums[j] == target:
                    key_dict[k]=[i,j]
                    return key_dict[k]


