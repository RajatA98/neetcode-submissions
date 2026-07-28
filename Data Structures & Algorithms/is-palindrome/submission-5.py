class Solution:
    def isPalindrome(self, s: str) -> bool:

        #traverse str from left and right 

        s = s.lower() #not case sensitive

        l = 0
        r = len(s) - 1

        alph = "abcdefghijklmnopqrstuvwxyz0123456789"

        while l <= r:
            #if the front and end are not equal return False
             # Skip non-alphanumeric characters on left
            while l < r and s[l] not in alph:
                l += 1
            # Skip non-alphanumeric characters on right
            while r > l and s[r] not in alph:
                r -= 1
            
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        #traverse through the whole string True
        return True
        