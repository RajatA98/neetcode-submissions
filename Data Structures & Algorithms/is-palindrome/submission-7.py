class Solution:
    def isPalindrome(self, s: str) -> bool:
        #since case - insesitive set input to all lowercase
        s = s.lower()
        #traverse from begining and end
        l = 0
        r = len(s) - 1

        while l <= r:
            #skip non alphnumeric
            while l < len(s) and not s[l].isalnum():
                l += 1
            while r >= 0 and not s[r].isalnum():
                r -= 1
            #if l pointer has now crossed over right pointer string is traversed 
            if l > r:
                break
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        #full string traversed return True
        return True

        