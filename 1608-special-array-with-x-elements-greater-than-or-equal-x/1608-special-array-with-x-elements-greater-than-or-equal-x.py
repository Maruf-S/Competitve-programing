class Solution:
    def specialArray(self, nums: List[int]) -> int:
        l,r = 0,1000
        def logic(num):
            count = 0
            for i in nums:
                if i >= num:
                    count += 1
            return count == num
        for i in range(1000):
            if logic(i):
                return i
        return -1
            