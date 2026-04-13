class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.minStack)==0:
            self.minStack.append(val)
        else:
            if val <= self.minStack[-1]:
                self.minStack.append(val)


    def pop(self) -> None:
        if len(self.stack) > 0 :
            val = self.stack.pop()
            if val == self.minStack[-1]:
                self.minStack.pop()

    def top(self) -> int:
        print(self.stack,self.stack[-1])
        return self.stack[-1]
        
    def getMin(self) -> int:
        print("get min", self.minStack,self.minStack[-1])
        return self.minStack[-1]
        
