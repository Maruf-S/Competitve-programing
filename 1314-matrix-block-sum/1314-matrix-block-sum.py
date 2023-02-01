
    
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        def solve(row, k):
            n = len(row)
            k = min(k, n)
            newRow = []
            right = k
            left = 0
            total = sum(row[0: right + 1])
            newRow.append(total)

            for index in range(1, n):
                if index > k:
                    total -= row[left]
                    left += 1

                if index < n - k:
                    right += 1
                    total += row[right]
                newRow.append(total)

            return newRow
        
        ans = [solve(row,k) for row in mat]
        ans = [solve(x, k) for x in zip(*ans)] 
        return [list(x) for x in zip(*ans)]

