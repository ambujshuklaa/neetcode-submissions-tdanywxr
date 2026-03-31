class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        key_dict={}
        key_dict1={}

        for i in s:
            if i in key_dict.keys():
                key_dict[i]=key_dict[i]+1
            else:
                key_dict[i]=1
        
        for i in t:
            if i in key_dict1.keys():
                key_dict1[i]=key_dict1[i]+1
            else:
                key_dict1[i]=1

        if len(key_dict) != len(key_dict1):
            return False

        for i in key_dict.keys():
            if  i in key_dict1.keys():
                if (key_dict[i] != key_dict1[i]):
                    return False
            else:
                return False 


        return True                     
        
        