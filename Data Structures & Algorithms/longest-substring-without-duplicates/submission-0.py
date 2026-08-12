class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #start with a window of 1 char 
        #use a set to keep track of the unique chars
        #if duplicated is dtected shif the window over

        maxSbtr = 0

        i = 0
        j = 0

        charSet = set()

        while j < len(s):
            #if current char in set shift window of same size over until char is unique 
            #or we have fully traversed the string 
            while s[j] in charSet:
                charSet.remove(s[i])
                i += 1
            
            charSet.add(s[j])
            maxSbtr = max(maxSbtr, j - i + 1)

            j += 1
        return maxSbtr
