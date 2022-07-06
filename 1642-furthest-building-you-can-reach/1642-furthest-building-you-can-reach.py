class Solution:
    def furthestBuilding(self, A, bricks, ladders):
        heap = []
        i = 0
        while ( i < len(A) - 1):
            d = A[i + 1] - A[i]
            if d > 0:
                heapq.heappush(heap,d)
            # Exhausted ladders
            if len(heap) > ladders:
                smallest = heapq.heappop(heap)
                bricks -= smallest
            if bricks < 0:
                return i
            i+=1
        return i
            
                
        