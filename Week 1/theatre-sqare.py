
def theater_square(values):
    # uncoveredL = values[0]%values[2]
    # uncoveredw = values[1]%values[2]
    coveredL = values[0]//values[2]
    coveredW = values[1]//values[2]
    print(coveredL+coveredW+2)
    pass

def inlt():
    return(list(map(int,input().split())))
theater_square(inlt())