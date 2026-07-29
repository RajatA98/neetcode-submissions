class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #traverse the heights
        #pointer from beg and end
        #track Area = min height * (r-l)
        #trax max

        l = 0
        r = len(heights) - 1
        maxArea = 0

        while l < r:
            area = min(heights[l],heights[r]) * (r-l)
            maxArea = max(area,maxArea)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxArea


        