"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
            
        intervals.sort(key=lambda x: x.start)
        
        s1 = intervals[0].start
        e1 = intervals[0].end
        
        for meeting in intervals[1:]:
            s2 = meeting.start
            e2 = meeting.end
            
            if s2 < e1:
                return False
                
            s1 = s2
            e1 = e2
            
        return True