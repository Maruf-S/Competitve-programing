class Solution(object):
    def maximumScore(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        score = 0
        h = []
        heapq.heappush(h,-a)
        heapq.heappush(h,-b)
        heapq.heappush(h,-c)
        while len(h) > 1:
            fele = heapq.heappop(h)
            secele = heapq.heappop(h)
            if fele + 1 < 0:
                heapq.heappush(h,fele + 1)
            if secele + 1 < 0:
                heapq.heappush(h,secele + 1)
            score += 1
        return score