class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        k=0
        key_dict={}

        for i in range (0,len(numbers),1):
            for j in range (i+1,len(numbers),1):
                if numbers[i] + numbers[j] == target:
                    # key_dict[k]=[numbers[i],numbers[j]]
                    key_dict[k]=[i+1,j+1]
                    # k=k+1
                    return key_dict[0]
        # print(key_dict.keys(),key_dict[0] )
        