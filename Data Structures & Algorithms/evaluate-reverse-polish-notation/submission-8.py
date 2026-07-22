class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #keep track of current total 
        #push numbers in a stack until u hit an operator 
        #pop values from a stack and use operator on all values 
        #push that value back into stack
        stack = []
        for t in tokens:
            
            if t == '+':
    
                rh = stack.pop()
                lh = stack.pop()
                cv = lh + rh
                stack.append(cv)
            elif t == '*':
                
                rh = stack.pop()
                lh = stack.pop()

                cv = lh * rh
                stack.append(cv)
            elif t == '-':
                
                rh = stack.pop()
                lh = stack.pop()
                cv = lh - rh
                stack.append(cv)
            elif t == '/':
                
                rh = stack.pop()
                lh = stack.pop()
                cv = int(lh / rh)
                stack.append(cv)
            else:
                stack.append(int(t))
        return stack.pop()