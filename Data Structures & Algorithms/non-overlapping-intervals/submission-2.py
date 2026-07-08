class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        e1 = intervals[0][1]
        res = 0
        for i in range(1, len(intervals)):
            s2, e2 = intervals[i]

            if s2 < e1:
                res += 1
                e1 = min(e1, e2)
            else:
                e1 = e2
        return res