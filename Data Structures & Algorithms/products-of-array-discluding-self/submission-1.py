class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        l = 0
        r = len(nums) - 1
        i = 0
        lp = [1] * len(nums)
        rp = [1] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                lp[i] = 1
            else:
                lp[i] = nums[i-1] * lp[i-1]
        for i in range(len(nums)-1,-1,-1):
            if i == len(nums) - 1:
                rp[i] = 1
            else:
                rp[i] = nums[i+1] * rp[i+1]
        for i in range(len(nums)):
            if i == len(nums)-1:
                ans[i] = lp[i]
            else:
                ans[i] = lp[i] * rp[i]

        return ans
            
        
            

        


        


        