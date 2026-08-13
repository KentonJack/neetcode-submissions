"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) < 2:
            return len(intervals)
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])
        c = 0
        res = 0
        s = 0
        e = 0
        while s < len(starts):
            if starts[s] < ends[e]:
                s += 1
                c += 1
            else:
                e += 1
                c -= 1
            res = max(res, c)
        return res