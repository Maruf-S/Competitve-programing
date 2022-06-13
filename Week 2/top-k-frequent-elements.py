def removeKdigits(num, k):
    """
    :type num: str
    :type k: int
    :rtype: str
    """
    n = []
    for i,j in enumerate(num[::-1]):
        n.append((i+1,int(j)))
    n.sort(key=lambda x: x[0]*x[1],reverse=True)
    print(n)