class StockSpanner:

    def __init__(self):
        self.s = []

    def next(self, price: int) -> int:
        spn = 1
        while self.s and self.s[-1][1] <= price:
            spn += self.s.pop()[0]
        self.s.append((spn,price))
        return spn

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)