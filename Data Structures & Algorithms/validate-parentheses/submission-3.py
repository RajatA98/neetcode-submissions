class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False
        open_paren = []
        paren_pairs = {}
        paren_pairs[')'] = '('
        paren_pairs[']'] = '['
        paren_pairs['}'] = '{'
        for p in s:
            if (p == '(') or (p == '[') or (p =='{'):
                open_paren.append(p)
            elif len(open_paren) == 0:
                return False
            elif paren_pairs[p] != open_paren[-1]:
                return False
            else:
                open_paren.pop()
        if len(open_paren):
            return False
        return True

                

        
                  