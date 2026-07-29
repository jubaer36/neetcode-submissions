"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])

        s , e , r , c = 0 ,0 ,0 ,0
        while s < len(starts):
            if starts[s] < ends[e]:
                c += 1
                s += 1
            else:
                c -= 1
                e += 1

            r = max(r , c)


        
        return r
        