"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        min_heap = []

        for interval in intervals:
            
            if len(min_heap)!=0 and min_heap[0] <= interval.start:
                print('avaibale room',interval.start,interval.end)
                heapq.heappop(min_heap)
            print('not avaibale room',interval.start,interval.end)
            heapq.heappush(min_heap, interval.end)

        return len(min_heap)

       