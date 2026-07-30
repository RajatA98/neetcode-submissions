class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #in this version the target is 0 and there are multiple solutions
        #start with sorting so we can us 2 sum approach
        #store tiplets in list
        triplets = []

        nums.sort()

        #travrse through nums

        for i, n in enumerate(nums):
            #target for 2 sum is 0 - cur num
            #since there are duplicate values let's skip starting with the duplicate value
            if i > 0 and n == nums[i-1]:
                continue
            target = 0 - n

            #check if target is >= 0 then no possible solution
            if target < 0:
                break
            #traverse rest of array and solve like 2 sum
            l = i+1
            r = len(nums) - 1
            while l < r:
                #get current sum of 2 pointers
                two_sum = nums[l] + nums[r]

                if two_sum < target:
                    l += 1
                elif two_sum > target:
                    r -= 1
                else:
                    triplet = [n,nums[l],nums[r]]
                    if triplet not in triplets:
                        triplets.append(triplet)
                    l += 1
                    r -= 1
        return triplets

