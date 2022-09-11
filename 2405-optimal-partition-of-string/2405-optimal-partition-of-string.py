class Solution:
    def partitionString(self, s: str) -> int:
        bucket = set()
        count = 1
        for i in s:
            if i in bucket:
                count += 1
                bucket.clear()
            bucket.add(i)
        return count