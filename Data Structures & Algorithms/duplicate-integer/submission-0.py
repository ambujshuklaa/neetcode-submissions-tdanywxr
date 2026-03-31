class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        key_dict ={}

        for i in nums:
            if i in key_dict.keys():
                key_dict[i]= key_dict[i] + 1
            else:
                key_dict[i]=1
        
        for i in key_dict.keys():
            if key_dict[i] > 1:
                return True
        
        return False;