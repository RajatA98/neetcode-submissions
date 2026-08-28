class Solution:
   def checkInclusion(self, s1: str, s2: str) -> bool:
        #we can use the sliding window approach 
        #window size = size of s1

        #permutation is where strings have the same char count
        #let's get the char count of the first string 

        s1_cnt = [0] * 26 #only 26 lowercase numbers

        for c in s1:
            s1_cnt[ord(c)-ord('a')] += 1
        
        #let's get the initial count of len s1 substring of s2

        s2_cnt = [0] * 26

        for c in s2[:len(s1)]:
            s2_cnt[ord(c)-ord('a')] += 1
        
        l = 0
        r = len(s1) - 1

        while r < len(s2):
            if s1_cnt == s2_cnt:
                return True
            s2_cnt[ord(s2[l])-ord('a')] -= 1
            l += 1
            r += 1
            if r < len(s2):
                s2_cnt[ord(s2[r])-ord('a')] += 1
        return False


        
        