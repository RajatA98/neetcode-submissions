class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #push values in stack if u see an operand pop top 2 
        stack = []

        for t in tokens:
            if t == '+':
                rh = stack.pop()
                lh = stack.pop()
                total = lh + rh
                stack.append(total)
            elif t == '-':
                rh = stack.pop()
                lh = stack.pop()
                total = lh - rh
                stack.append(total)
            elif t == '*':
                rh = stack.pop()
                lh = stack.pop()
                total = lh * rh
                stack.append(total)
            elif t == '/':
                rh = stack.pop()
                lh = stack.pop()
                total = int(lh / rh)
                stack.append(total)
            else:
                stack.append(int(t))
        return stack[-1]
