import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #usa a hasmap to get the cound of each number 
        #heapify and pick the top k

        n_cnt = {}

        for num in nums:
            if num in n_cnt:
                n_cnt[num] += 1
            else:
                n_cnt[num] = 1

        heap = []

        for n , f in n_cnt.items():
            heapq.heappush(heap, (f,n))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for f, num in heap]

        
        