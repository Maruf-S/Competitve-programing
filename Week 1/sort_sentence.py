def extractNum(a):
    return int(a[-1])
def removeNumber(string):
    return string[:-1]
class Solution(object):
    def sortSentence(self, s):
        toList = s.split(" ")
        toList.sort(key=extractNum)
        return(" ".join(list(map(removeNumber,toList))))