class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Using teh sliding window approach 
        #start with windo size 1
        #expand from the right 
        #Track freq of each char
        alph_freq = [0] * 26
        l = 0
        r = 0 
        max_freq = 0
        result = 0
        while r < len(s):
            wSize = r - l + 1
            alph_freq[ord(s[r]) - ord('A')] += 1
            max_freq =  max(max_freq,alph_freq[ord(s[r]) - ord('A')])
            #check if we can perform valid swaps 
            swaps =  wSize - max_freq
            while swaps > k:
                alph_freq[ord(s[l]) - ord('A')] -= 1
                l += 1
                wSize = r - l + 1
                swaps = wSize - max_freq
            
            result = max(result,wSize)
            r += 1
        return result



        