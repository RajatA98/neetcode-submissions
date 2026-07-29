class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #Traverse the numbers list using 2 pointers
        #one starting from the idx 0 and one starting at idx len(numbers) - 1
        l = 0
        r = len(numbers) - 1


        while l < r:
            #compute the current sum
            c_sum = numbers[l] + numbers[r]

            #if sum > target decriment right pointer
            #if sun < target increment left pointer
            #if == return idxs

            if c_sum > target:
                r -= 1
            elif c_sum < target:
                l += 1
            else:
                return [l+1,r+1]