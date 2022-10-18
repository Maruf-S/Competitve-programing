class Solution:
    def numSplits(self, st: str) -> int:
        unique_count_front = [0] * len(st)
        unique_count_back = [0] * len(st)
        s = set()
        for i in range(len(st)):
            s.add(st[i])
            unique_count_front[i] = len(s)
        s = set()
        for i in range(len(st) - 1,-1,-1):
            s.add(st[i])
            unique_count_back[i] = len(s)
        count = 0
        for i in range(len(st) - 1):
            count += unique_count_front[i] == unique_count_back[i + 1]
        # print(unique_count_front,unique_count_back)
        return count