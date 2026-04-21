class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        key_dict={}

        for i in set(s):
            key_dict[i]=0

        # for i in range(0, len(s),1):
        #     if key_dict[s[i]] == []:
        #         l = [i]
        #         key_dict[s[i]] = l
            
        #     else:
        #         l = [i]
        #         key_dict[s[i]] = key_dict[s[i]] + l

        # for i in key_dict.keys():
        #     for j in range (0, len(i),1) :
        #         print(i,key_dict[i], j+1, j, key_dict[i][j+1] - key_dict[i][j])
            
        l = 0
        r = 0

        res = 0

        while (r < len(s) and l < len(s)):
            key_dict[s[r]]= key_dict[s[r]] + 1
            window = r - l + 1 

            print(f'window {window} and max {max(key_dict.values())} and old res', res)
            
            if window - max(key_dict.values()) <= k:
                res = max(window, res)
                print('new res',res)
                r = r + 1
            else:
                key_dict[s[l]]= key_dict[s[l]] - 1
                l = l + 1
                r = r + 1
        
        print(res)

        return res

                


            

        