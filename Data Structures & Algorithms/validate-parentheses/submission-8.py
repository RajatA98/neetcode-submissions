class Solution:
    def isValid(self, s: str) -> bool:
        # map the parenthesis pairs
        paren_pair = {")": "(", "]":"[", "}": "{"}

        open_p = []

        #push all open paren in stack

        for p in s:
            if p in paren_pair:
                if open_p == [] or paren_pair[p] != open_p[-1]:
                    return False
                else:
                    open_p.pop()
            else:
                open_p.append(p)
        
        return open_p == []
        