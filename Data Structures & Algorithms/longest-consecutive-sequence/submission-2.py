class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #white iterating through nums check neighbors of current val
        #store vals in a set so we can search for neighbors 

        numSet = set(nums)

        #keep track of current sequence

        cur_seq = 0

        longest_seq = 0

        for n in numSet:
            if n-1 not in numSet:
                cur_seq = 1
                while n + cur_seq in numSet:
                    cur_seq += 1
                longest_seq = max(longest_seq,cur_seq)
        return longest_seq
        