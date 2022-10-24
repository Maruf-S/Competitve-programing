class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def numberToBase(n, b):
            if n == 0:
                return [0]
            digits = []
            while n:
                digits.append(int(n % b))
                n //= b
            return digits[::-1]
        def isPalindrome(s):
            return s == s[::-1]
        for i in range(2,n-1):
            if not isPalindrome(numberToBase(n,i)):
                return False
        return True