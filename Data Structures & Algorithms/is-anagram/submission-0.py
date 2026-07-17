class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_letter_count = {}
        t_letter_count = {}
        for sl in s:
            if sl in s_letter_count:
                s_letter_count[sl] += 1
            else:
                s_letter_count[sl] = 1
        for tl in t:
            if tl in t_letter_count:
                t_letter_count[tl] += 1
            else:
                t_letter_count[tl] = 1
        for l in s:
            if l not in t:
                return False
            elif s_letter_count[l] != t_letter_count[l]:
                return False
        return True
        