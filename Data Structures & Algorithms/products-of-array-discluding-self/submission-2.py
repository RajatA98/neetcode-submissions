class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #travese l - r calculate the product left of current i
        #traverse r - l calculate the product right of current
        #calculate the ans

        lp = [1] * len(nums)
        rp = [1] * len(nums)
        ans = []

        for i in range(1,len(nums)):
            lp[i] = lp[i-1] * nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            rp[i] = rp[i+1] * nums[i+1]
        for i in range(len(nums)):
            ans.append(lp[i]*rp[i])
        return ans
        