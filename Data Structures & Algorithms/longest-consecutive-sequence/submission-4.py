class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = sorted(list(set(nums)))
        k=0
        key_dict={}
        for i in range (0, len(nums),1):
            print(i,nums[i],k)
            if (i + 1) !=len(nums):
                if (nums[i+1] - nums[i] == 1 ) and (i + 1 < len(nums)):
                    l= []
                    l.append(nums[i])
                    if k in key_dict.keys():
                        key_dict[k]= key_dict[k] + l
                    else:
                        key_dict[k]=l
                else:
                    l= []
                    l.append(nums[i])
                    if k in key_dict.keys():
                        key_dict[k]= key_dict[k] + l
                    else:
                        key_dict[k]=l
                    k=k+1
            else:
                if (nums[i] - nums[i-1] == 1 ):
                    l= []
                    l.append(nums[i])
                    if k in key_dict.keys():
                        key_dict[k]= key_dict[k] + l
                    else:
                        key_dict[k]=l
                else:
                    l= []
                    l.append(nums[i])
                    k=k+1
                    if k in key_dict.keys():
                        key_dict[k]= key_dict[k] + l
                    else:
                        key_dict[k]=l

        max = 0
        index=0
        for i in key_dict.keys():
            if len(key_dict[i]) > max:
                max=len(key_dict[i])
                index=i
        
        print(index,max)
        return max





