class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW,COL = len(matrix), len(matrix[0])
        t = 0
        b = ROW - 1
        while t <= b:
            mid = (t + b)//2
            if target < matrix[mid][0]:
                b = mid - 1
            elif target > matrix[mid][-1]:
                t = mid + 1
            else:
                break
        if t > b:
            return False
        row = (t + b)//2
        l = 0
        r = COL - 1
        while l <= r:
            mid = (l + r)//2
            if matrix[row][mid] < target:
                l = mid + 1
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                return True
        return False