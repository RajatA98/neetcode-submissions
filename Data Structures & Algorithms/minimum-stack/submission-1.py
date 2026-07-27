class MinStack:

    def __init__(self):
        #let's keep a regualr stack
        #and a min stack to keep track of the current min value in the whole stack

        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        #if the stack is empty or the current val is < cur min push val

        if self.minStack == [] or val < self.minStack[-1]:
            self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[-1])
            
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
