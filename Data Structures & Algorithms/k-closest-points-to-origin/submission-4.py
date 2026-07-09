class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point):
            x, y = point
            return math.sqrt(x**2 + y**2)
        
        heap = []
        for point in points:
            heapq.heappush(heap, (-distance(point), point))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        while heap:
            _, point = heapq.heappop(heap)
            res.append(point)
        
        return res
