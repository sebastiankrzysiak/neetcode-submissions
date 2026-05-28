class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []

        for key, val in count.items():
            heap.append((-val, key))

        heapq.heapify(heap)
        res = []
        for _ in range(k):
            _, key = heapq.heappop(heap)
            res.append(key)
        
        return res