class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n_f = {}
        buckets = [[] for freq in range(len(nums) + 1) ]
        ans = []
        for n in nums:
            if n in n_f:
                n_f[n] += 1
            else:
                n_f[n] = 1
        for num, freq in n_f.items():
            buckets[freq].append(num)

        for freq in range(len(buckets) -1, 0, -1):
            for num in buckets[freq]:
                ans.append(num)
                if len(ans) == k:
                    return ans
                
        return ans
        