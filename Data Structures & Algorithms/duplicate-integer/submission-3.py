class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_cnt = {}
        for n in nums:
            if n in num_cnt:
                return True
            else:
                num_cnt[n] = 1
        return False