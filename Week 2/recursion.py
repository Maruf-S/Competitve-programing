def getOne(x):
    print(1)


def getTwo(x):
    getOne(0)
    print(2)


def test():
    # x = getTwo()
    # getOne(y)
    getTwo(1)


test()
