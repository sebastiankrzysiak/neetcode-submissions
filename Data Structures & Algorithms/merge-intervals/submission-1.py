class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for s2, e2 in intervals[1:]:
            s1, e1 = res[-1]

            if s2 <= e1:
                res[-1] = [s1, max(e1, e2)]
            else:
                res.append([s2, e2])
        
        return res