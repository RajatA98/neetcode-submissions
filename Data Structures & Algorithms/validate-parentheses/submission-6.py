class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            if c == ')' or c == ']' or c == '}':
                if stack == []:
                    return False
            if c == ')':
                top = stack.pop()
                if top != '(':
                    return False
            if c == ']':
                top = stack.pop()
                if top != '[':
                    return False
            if c == '}':
                top = stack.pop()
                if top != '{':
                    return False
        return stack == []