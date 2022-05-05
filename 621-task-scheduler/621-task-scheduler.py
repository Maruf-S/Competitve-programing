class Solution(object):
    def leastInterval(self, tasks, n):
        from collections import Counter
        count = Counter(tasks)
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()

        while maxHeap or q:
            time+=1
            if maxHeap:
                # Pop le max count
                # Minimum
                cnt  = heapq.heappop(maxHeap) + 1
                if(cnt!=0):
                    # task hasnt finished processing
                    # so we'll add it to the queue to wait for it's time
                    q.append([cnt,time+n])

            if(q and q[0][1] == time):
                # Our task can run now
                heapq.heappush(maxHeap,q.popleft()[0])
        return time