class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        added = False

        for i, (start, end) in enumerate(intervals):
            if start > newInterval[0]:
                intervals.insert(i, newInterval)
                added = True
                break
        
        if not added:
            intervals.append(newInterval)
        
        res = [intervals[0]]

        for j, (s2, e2) in enumerate(intervals):
            if j == 0:
                continue
            s1, e1 = res[-1]

            if e1 >= s2:
                res[-1] = [s1, max(e1, e2)]
            else:
                res.append([s2, e2])

        return res