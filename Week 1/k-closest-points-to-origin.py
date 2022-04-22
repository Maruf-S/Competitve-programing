def sort_relative_to_distance(a):
    return a[0]
class Solution(object):
    def ge_distance_f_origin(self,point):
        import math
        return math.sqrt(point[0]**2+point[1]**2)
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        n = len(points)
        distances = [(0,0)]*n
        for i in range(n):
            distances[i] = (self.ge_distance_f_origin(points[i]),points[i])
        distances.sort(key=sort_relative_to_distance)
        return list(map(lambda x: x[1], distances[:k]))