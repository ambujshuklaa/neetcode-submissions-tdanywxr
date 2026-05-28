class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # key_dict={}

        # for i in nums:
        #     if i in key_dict.keys():
        #         key_dict[i]=key_dict[i] + 1
        #     else:
        #         key_dict[i]=1

        # output = []

        # for i in key_dict.keys():
        #     output.append(key_dict[i])
        
        # output = sorted(output,reverse=True)

        # final_output=[]

        # for i in key_dict.keys():
        #     if  key_dict[i] in output[:k]:
        #         final_output.append(i)

        # return final_output     


        key_dict = {}

        freq = [[] for i in range(len(nums) + 1)]

        for i in nums:
            key_dict[i] = 1 + key_dict.get(i,0)

        # print(key_dict)  

        for n,c in key_dict.items():
            # print(n,c)
            freq[c].append(n)
        

        output=[]
        print(freq)

        for i in range(len(freq)-1,0,-1):
            if freq[i] != [] and len(output)!=k:
                for j in freq[i]:
                    output.append(j)
            elif len(output)==k:
                break

        print(output)
        return output


        