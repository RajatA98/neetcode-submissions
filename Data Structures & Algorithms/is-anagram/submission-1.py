class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_cnt_s = {}
        char_cnt_t = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in char_cnt_s:
                char_cnt_s[s[i]] = 1
            else:
                char_cnt_s[s[i]] += 1
            if t[i] not in char_cnt_t:
                char_cnt_t[t[i]] = 1
            else:
                char_cnt_t[t[i]] += 1
        if char_cnt_s == char_cnt_t:
            return True
        return False
        