powers = set([pow(3, i) for i in xrange(200)])
class Solution(object):
    def isPowerOfThree(self, num):
        return num in powers