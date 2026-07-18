from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        length = 0

        for n in numSet:
            #check left neighbor
            if (n - 1) not in numSet:
                #if not in then start of sequence
                length = 1
                while (n+length) in numSet:
                    length += 1
            longest = max(length, longest)
        return longest

            

        