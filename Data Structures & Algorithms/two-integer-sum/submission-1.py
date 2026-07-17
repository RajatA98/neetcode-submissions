class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #hash numbers to index
        #iterate through has table 
        #if target - current num in haah return list of indexes
        num_index = {}
        solution = []
        for  i in range(len(nums)):
                if (target - nums[i]) in num_index:
                    solution = [num_index[target-nums[i]], i]
                    return solution
                num_index[nums[i]] = i
    
        

       
        