class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        l = 0
        r = len(nums) - 1
        i = 0
        while i < len(nums):
            while l < i:
                ans[i] = ans[i] * nums[l]
                l += 1
            while r > i:
                ans[i] = ans[i] * nums[r]
                r -= 1

            i += 1
            l = 0
            r = len(nums) - 1
        return ans
            

        


        


        