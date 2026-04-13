class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output=[0] * len(temperatures)

        for i in range (0,len(temperatures),1):
            if len(stack)==0:
                stack.append([temperatures[i],i])
            else:
                l= len(stack)
                print(l-1,stack[l-1],stack[l-1][0], temperatures[i])

                if temperatures[i] <= stack[l-1][0]:
                    print('Stack appened is ',stack,temperatures[i])
                    stack.append([temperatures[i],i])
                
                else:
                    for j in range(len(stack)-1,-1,-1):
                        if temperatures[i] > stack[j][0]:
                            val = stack.pop()
                            print('within loop',stack,j, val)
                            output[val[1]]=i - val[1]
                    stack.append([temperatures[i],i])

        print(output)

        return output