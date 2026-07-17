class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
          n_i = {}
          for i in range(len(nums)):
            k = target - nums[i]
            if k in n_i:
                return [n_i[k],i]
            n_i[nums[i]] = i
        
        