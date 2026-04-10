class Solution:
    def isValid(self, s: str) -> bool:
        
        sol= []

        if len(s)<=1:
            return False


        for i in s:
            if i in ('(','{','['):
                sol.append(i)
                print(sol)
            else:
                if len(sol)!=0:
                    if (sol[-1] == '{' and i=='}') or (sol[-1]=='[' and i == ']') or (sol[-1] =='(' and i == ')'):
                        sol.pop()
                        print(i,sol)
                        
                    else :
                        return False
                else:
                    return False
        
        if len(sol)==0:
            return True
        else:
            return False