class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        mid = (i + j) // 2 
        while i <= j:
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                j = mid -1
                mid = (i + j) // 2
            else:
                i = mid + 1
                mid = (i + j) // 2
        return -1