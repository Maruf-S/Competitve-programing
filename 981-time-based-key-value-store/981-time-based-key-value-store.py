class TimeMap:

    def __init__(self):
        self.tm = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tm[key].append((value,timestamp))
    
    def get(self, key: str, timestamp: int) -> str:
        ls = self.tm[key]
        l,r = 0,len(ls) - 1
        res = ""
        while l <= r:
            m = l + (r-l)//2
            if ls[m][1] <= timestamp:
                res = ls[m][0]
                l = m + 1
            else:
                r = m - 1
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)