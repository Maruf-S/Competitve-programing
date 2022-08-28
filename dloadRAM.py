import heapq
def test(n, k, a, b):
    h = []
    for i,j in zip(a,b):
        heapq.heappush(h,(i,j))
    total = k
    while h:
        cost, gain = heapq.heappop(h)
        if total - cost < 0:
            break
        total += gain
    print(total)

def inp():
    return(int(input()))


def inlt():
    return(list(map(int, input().split())))


for i in range(inp()):
    f = inlt()
    a = inlt()
    b = inlt()
    test(f[0], f[1], a, b)

# 1
# 5 8
# 128 64 32 16 8
# 128 64 32 16 8