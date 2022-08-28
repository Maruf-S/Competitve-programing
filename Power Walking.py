from collections import defaultdict
t = int(input())

for i in range(t):
    k = int(input())
    a = list(map(int, input().split()))
    d = defaultdict(int)
    for i in range(k):
        d[a[i]] += 1

    for i in range(1, k+1):
        print(max(i, len(d)), end=" ")
    print()