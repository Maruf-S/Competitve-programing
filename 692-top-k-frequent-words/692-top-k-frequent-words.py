class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        def compare(item1, item2):
            if item1[0] < item2[0]:
                return -1
            elif item1[0] > item2[0]:
                return 1
            else:
                if item1[1] < item2[1]:
                    return -1
                else:
                    return 1
        uniqueElements = {}
        for i in words:
            uniqueElements[i] = uniqueElements.get(i,0) + 1
        minHeap = []
        class Element:
            def __init__(self, count, word):
                self.count = count
                self.word = word

            def __lt__(self, other):
                if self.count == other.count:
                    return self.word > other.word
                return self.count < other.count

            def __eq__(self, other):
                return self.count == other.count and self.word == other.word

        for key, value in uniqueElements.items():
            heapq.heappush(minHeap, Element(value, key))
            if(len(minHeap) > k):
                heapq.heappop(minHeap)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(minHeap).word)
        return res[::-1]