class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        key_dict={}

        for i in nums:
            if i in key_dict.keys():
                key_dict[i]=key_dict[i] + 1
            else:
                key_dict[i]=1

        output = []

        for i in key_dict.keys():
            output.append(key_dict[i])
        
        output = sorted(output,reverse=True)

        final_output=[]

        for i in key_dict.keys():
            if  key_dict[i] in output[:k]:
                final_output.append(i)

        return final_output              

        