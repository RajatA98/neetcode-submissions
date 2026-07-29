class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort the input list
        nums.sort()
        #-4 -1 -1 0 1 2
        # i: -4 -4 -4
        # j: -1 -1 0
        # k: 2  2
        #sum: -3 -3 
        #left ptr at 0 and one at 1
        #right ptr at end of nums

        i = 0
        j = 1
        k = len(nums) - 1

        #store ans

        ans = []

        #while traversing through nums
        #check sum
        

       

        #if sum > 0 decriment right ptr

        #if 0 push to ans and then move all three ptrs until nums traversed

        while j < k and i < j:
            #calculate current sum
            c_sum = nums[i] + nums[j] + nums[k]

            if c_sum < 0:
                j += 1
        
            elif c_sum > 0:
                k -= 1
            else:
                triple = [nums[i],nums[j],nums[k]]
                if triple not in ans:
                    ans.append(triple)
                j += 1
                k -= 1

            if j >= k:
                i += 1
                j = i + 1
                k = len(nums) - 1

            
        return ans

        