def bubbleSort(array):
    length = len(array)
    for i in range(length):
        for j in range(length-i-1):
            if(int(array[j][-1])>int(array[j+1][-1])):
                array[j], array[j + 1] = array[j + 1], array[j]
    return (array)
def removeNumber(string):
    return string[:-1]
class Solution(object):
    def sortSentence(self, s):
        toList = s.split(" ")
        sorted = bubbleSort(toList)
        return(" ".join(list(map(removeNumber,sorted))))