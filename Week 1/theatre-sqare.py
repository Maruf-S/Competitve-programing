import math
def theater_square(values):
    l = math.ceil(values[0]/values[2])
    w = math.ceil(values[1]/values[2])
    print(l*w)
    pass

def inlt():
    return(list(map(int,input().split())))
theater_square(inlt())