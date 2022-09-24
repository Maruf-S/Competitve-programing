class Solution(object):
    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """
        def multiply(X, Y):
            return [[sum(a*b for a,b in zip(X_row,Y_col)) % 1000000007 for Y_col in zip(*Y)] for X_row in X]
        
        ans, acc, level = [[1], [2], [1]], 1, 1
        while acc < n:
            M = 2 ** (level + 1)

            # number of matrix production in this level
            x = take = min(n, M - 1) - acc

            mat = [[M, 1, 0], [0, 1, 1], [0, 0, 1]]

            # for example
            # num^13 = num * num^4 * num^8
            # num^6 = num^2 * num^4
            while x > 0:
                if x & 1: ans = multiply(mat, ans)
                mat, x = multiply(mat, mat), x >> 1

            acc, level = acc + take, level + 1
        
        return ans[0][0]