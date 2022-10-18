# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        answer = [[-1 for _ in range(n)] for i in range(m)]
        dirn = [0,1]
        def changeDirn(dirn):
            dirn[0],dirn[1] = dirn[1], -dirn[0]
            return dirn
        def inBound(r,c):
            if 0 <= r < m and 0 <= c < n:
                return True
        current_x,current_y = 0,0
        while head:
            answer[current_x][current_y] = head.val
            if not inBound(current_x + dirn[0],current_y + dirn[1]) or answer[current_x + dirn[0]][current_y + dirn[1]] != -1:
                dirn = changeDirn(dirn)
            current_x += dirn[0]
            current_y += dirn[1]
            # print(current_x,current_y,dirn)
            head = head.next
        return answer