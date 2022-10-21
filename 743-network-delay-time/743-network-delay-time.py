class Solution:
    def networkDelayTime(self, netTimes: List[List[int]], n: int, k: int) -> int:
        times = [float("inf")] * n
        times[k - 1] = 0
        for _ in range(n - 1):
            tempTimes = times[:]
            for fr,to,weight in netTimes:
                if times[fr - 1] + weight < tempTimes[to - 1]:
                    tempTimes[to - 1] = times[fr - 1] + weight
            times = tempTimes
        max_time = max(times)
        if max_time == float("inf"):
            # Unable to reach everyone
            return -1
        return max_time