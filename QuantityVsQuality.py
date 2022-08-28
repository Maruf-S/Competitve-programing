import heapq


def test(n, s):
    s.sort()
    blue,red,l,r = s[0],0,1,n-1
    while l < r:
        blue += s[l]
        red  += s[r]
        if red > blue:
            return print("YES")
        l += 1
        r -= 1
    print("NO")
def inp():
    return(int(input()))


def inlt():
    return(list(map(int, input().split())))


for i in range(inp()):
    n = inp()
    s = inlt()
    test(n, s)
