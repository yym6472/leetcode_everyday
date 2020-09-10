"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        # write your code here
        def dist(p1, p2):
            return (p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2
        class PointWrapper(object):
            def __init__(self, point):
                self.point = point
            def __lt__(self, other):
                dist_self = dist(self.point, origin)
                dist_other = dist(other.point, origin)
                return dist_self > dist_other or \
                       dist_self == dist_other and self.point.x > other.point.x or \
                       dist_self == dist_other and self.point.x == other.point.x and self.point.y > other.point.y
            def __gt__(self, other):
                return not self.__lt__(other) and not self.__eq__(other)
            def __eq__(self, other):
                return self.point.x == other.point.x and \
                    self.point.y == other.point.y
        heap = []
        from heapq import heappush, heappop
        for point in points:
            heappush(heap, PointWrapper(point))
            if len(heap) > k:
                heappop(heap)
        results = []
        while heap:
            results.append(heappop(heap).point)
        results.reverse()
        return results