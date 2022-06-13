from cmath import log


def mergeSort(l):
    n = len(l)
    if(n == 1):
        return l
    left = l[:n//2]
    right = l[n//2:]
    mergeSort(left)
    mergeSort(right)
    # Two iterators for traversing the two halves
    i = 0
    j = 0

    # Iterator for the big List (the one containing the left and right)
    k = 0
    #! This doesn't exec until l and r portion of l are sorted
    print(l)
    #! Sorting a 2 sorted list always
    #! But how??? remember the tree... if the list has 2 elements then just comparing 2
    #! fuck me ded when will i understand this shit
    while i < len(left) and j < len(right):
        # Comparing them Both then adding the said element in it's place
        if left[i] <= right[j]:
            # The value from the left half has been used
            l[k] = left[i]
            # Move the iterator forward
            i += 1
        else:
            l[k] = right[j]
            j += 1
        # Move to the next slot
        k += 1
    #! Merge elements that were skipped (list ended on one of the elements)
    if(i < len(left)):
        # do the rest L
        while(i < len(left)):
            l[k] = left[i]
            i += 1
            k += 1
    else:
        # fill the rest R
        while(j < len(right)):
            l[k] = right[j]
            j += 1
            k += 1

    print(i, j, k)


x = [1, 8, 6, 31, 23, 2, 2, 32, 2, 32, 2322, ]
mergeSort(x)

print(x)
