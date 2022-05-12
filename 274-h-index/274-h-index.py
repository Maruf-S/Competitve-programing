class Solution:
    def hIndex(self, citations):
        citations.sort(reverse = True)
        for i in range(len(citations)):
            if i + 1 >= citations[i]:
                return max(i, citations[i])
        return len(citations)