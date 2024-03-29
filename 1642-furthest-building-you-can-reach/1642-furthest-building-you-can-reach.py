class Solution:
    def furthestBuilding(self, A, bricks, ladders):
        heap = []
        i = 0
        while ( i < len(A) - 1):
            d = A[i + 1] - A[i]
            if d > 0:
                if d <= bricks:
                    bricks -= d
                    heapq.heappush(heap,-d)
                elif ladders>0:
                    if len(heap) > 0:
                    # Recover max amnt of bricks 
                        largest_leap = -heap[0]
                        if(largest_leap > d):
                            bricks += largest_leap
                            heapq.heappop(heap)
                            heapq.heappush(heap,-d)
                            bricks -= d
                    ladders-=1
                else:
                    break
            i+=1
        return i
            

# # Min heap solution
# class Solution:
#     def furthestBuilding(self, A, bricks, ladders):
#         heap = []
#         i = 0
#         while ( i < len(A) - 1):
#             d = A[i + 1] - A[i]
#             if d > 0:
#                 heapq.heappush(heap,d)
#             # Exhausted ladders
#             if len(heap) > ladders:
#                 smallest = heapq.heappop(heap)
#                 bricks -= smallest
#             if bricks < 0:
#                 return i
#             i+=1
#         return i
            
                
        