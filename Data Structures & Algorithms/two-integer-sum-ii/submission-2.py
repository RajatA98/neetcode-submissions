class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #since sorted we can traverse the numbers going form beg and end 
        l = 0 
        r = len(numbers) -  1

        while l < r:
            #calculate the current sum
            c_sum = numbers[l] + numbers[r]

            if c_sum < target:
                #sum is smaller move left pointer
                l += 1
            elif c_sum > target:
                #sum is larger mover right pointer
                r -= 1
            else:
                #found sum return idx
                return [l+1,r+1]

        