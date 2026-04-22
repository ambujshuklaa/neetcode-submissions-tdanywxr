class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:


        size = len(s1)

        key_dict = {}

        check_dict={}

        for i in s1:
            if i in key_dict.keys():
                key_dict[i] = key_dict[i] + 1
            else:
                key_dict[i] = 1
        
        l = 0
        r = 0

        while (r < len(s2)):
            if r < len(s1) :
                if s2[r] in check_dict.keys():
                    check_dict[s2[r]] = check_dict[s2[r]] + 1
                else:
                    check_dict[s2[r]]=1
                print(r,check_dict)
            else:
                
                if key_dict == check_dict :
                    print('key dict',key_dict)
                    print('check_dict ',check_dict)
                    return True
                else:
                    # if s2[l] in check_dict.keys():
                    print('previos dict value ',check_dict,check_dict[s2[l]], s2[l],l)
                    if check_dict[s2[l]] > 1 :
                        check_dict[s2[l]] = check_dict[s2[l]] - 1
                    else:
                        check_dict.pop(s2[l])
                    
                    l= l + 1
                    # print('check dict s[r]',s2[r],check_dict )

                    if s2[r] in check_dict.keys():
                        check_dict[s2[r]] = check_dict[s2[r]] + 1
                    else:
                        check_dict[s2[r]]=1                    
                    print('new check dict',check_dict )
            print('r and r + 1', r , r+ 1, len(s2))
            r = r + 1        

        if key_dict == check_dict :
                    print('key dict',key_dict)
                    print('check_dict ',check_dict)
                    return True   
        return False


        