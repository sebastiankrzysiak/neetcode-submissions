class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)
        heap = [num for num, _ in count.items()]
        heapq.heapify(heap)

        while heap:
            first = heap[0]
            for num in range(first, first + groupSize):
                if num not in count:
                    return False
                count[num] -= 1
                if count[num] == 0:
                    if num != heap[0]:
                        return False
                    heapq.heappop(heap)
        
        return True