class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # key_dict={}
        if len(s)==1:
            return 1
        
        if len(s)==0:
            return 0
        
        # for i in range(0, len(s),1):
        #     o = ''
        #     for j in range(i, len(s),1):
        #         if s[j] not in o:
        #             o= o + s[j]
        #             if o in key_dict.keys():
        #                 key_dict[o] = key_dict[o] + 1 
        #             else:
        #                 key_dict[o]= 1
        #         else:
        #             break


        # max_substring = ''  
        # max_count = 0   
        # output_dict={}                   
        # for i in key_dict.keys():
        #     if (len(i) > len(max_substring)):
        #         max_substring = i
        #         max_count = key_dict[i]

        # output_dict[max_substring] = key_dict[max_substring]

        # output_substring=''
        # for i in output_dict.keys():

        #     if (len(i) > len(output_substring)):
        #         output_substring=i



        # print('Max substring',output_substring)
        # return len(output_substring)


        key_dict={}

        l = 0 
        r = 0
        maxLength = 0

        while (r< len(s)):

            if s[r] not in key_dict.keys():
                key_dict[s[r]]= r
                maxLength= max(maxLength, r - l + 1)
                print('insert ',maxLength)
                r = r + 1
            else:
                print('before if ',l, key_dict[s[r]])
                if l <= key_dict[s[r]] :
                    l = key_dict[s[r]] + 1
                    key_dict[s[r]] = r

                    # maxLength= max(maxLength, r - l)
                    r = r + 1
                    print('no change ',maxLength)
                else:
                    key_dict[s[r]]= r
                    maxLength= max(maxLength, r - l + 1)
                    print('else case ',maxLength)
                    r = r + 1

        print(maxLength)
        return maxLength

        # if len(s) == 0:
        # return 0

        # key_dict = {}
        # l = 0
        # r = 0
        # maxLength = 0

        # while r < len(s):
        #     if s[r] not in key_dict or key_dict[s[r]] < l:
        #         # Add the character to the dictionary and calculate maxLength
        #         key_dict[s[r]] = r
        #         maxLength = max(maxLength, r - l + 1)
        #         r += 1
        #     else:
        #         # Move the left pointer to exclude the duplicate
        #         l = key_dict[s[r]] + 1
        #         key_dict[s[r]] = r
        #         r += 1

        # return maxLength










        