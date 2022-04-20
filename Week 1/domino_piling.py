def invr():
    return(map(int, input().split()))


inputs = list(invr())
number_of_cells = inputs[0]*inputs[1]
print(number_of_cells//2)
