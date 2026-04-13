class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        self.stack=[]

        for i in tokens:
            if i not in ('+','-','*','/'):
                self.stack.append(i)
                print(self.stack)
            else:
               
                for j in range (0,2,1):
                    print("j is ", j)
                    if j ==0:
                        val = int(self.stack.pop())
                    else:
                        if i == '+':
                            val = int(self.stack.pop()) + val
                        elif i == '-':
                            val = int(self.stack.pop()) - val
                        elif i == '*':
                            val = int(self.stack.pop()) * val
                        elif i == '/':
                            val = int(self.stack.pop()) / val
                print('print val ',val, self.stack)
                self.stack.append(str(int(val)))
        
        print(self.stack)

        return int(self.stack.pop())