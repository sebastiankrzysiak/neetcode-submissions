class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)
        heap = [(num, cnt) for num, cnt in count.items()]
        heapq.heapify(heap)

        while heap:
            prev = None
            history = []
            for i in range(groupSize):
                if not heap:
                    return False
                num, cnt = heapq.heappop(heap)
                if i == 0:
                    prev = num
                else:
                    if prev + 1 != num:
                        return False
                    prev = num
                cnt -= 1
                if cnt:
                    history.append((num, cnt))
            for num, cnt in history:
                heapq.heappush(heap, (num, cnt))
        
        return True