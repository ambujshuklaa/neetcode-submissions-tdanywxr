class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]

        pair = sorted([[p,s] for p,s in zip(position,speed)])

        print(pair)



        for j in range (len(pair)-1, -1, -1):
            if j == len(pair)-1:
                stack.append(pair[j])

            benchMark = (target - stack[len(stack)-1][0]) / stack[len(stack)-1][1]

            if (target - pair[j][0]) / pair[j][1] > benchMark:
                stack.append(pair[j])
        
        print(stack)
        return len(stack)

        