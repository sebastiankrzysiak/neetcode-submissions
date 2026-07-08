"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        heap = []
        intervals.sort(key=lambda x : x.start)

        for interval in intervals:
            start = interval.start
            end = interval.end
            if not heap:
                heapq.heappush(heap, end)
            else:
                if heap and heap[0] <= start:
                    heapq.heappop(heap)
                heapq.heappush(heap, end)
        print([[interval.start, interval.end] for interval in intervals])
        return len(heap)