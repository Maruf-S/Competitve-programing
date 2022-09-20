class Solution:
    def isPossibleDivide(self, hand: List[int], k: int) -> bool:
        count = Counter(hand)
        h = (list(count.keys()))
        heapify(h)
        if len(hand) % k !=0:
            return False
        while h:
            m = h[0]
            for i in range(m,m + k):
                if count[i] > 0:
                    count[i] -= 1
                else:
                    if i != m:
                        return False
                    else:
                        break
                if count[i] == 0 and h[0] == i:
                    heappop(h)
        return True