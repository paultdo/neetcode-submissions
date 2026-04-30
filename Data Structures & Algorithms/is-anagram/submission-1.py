class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sLenDict = dict()
        tLenDict = dict()

        if len(s) == len(t):

            for i in range(len(s)):
                if not sLenDict.get(s[i]):
                    sLenDict.update({s[i]: 1})
                else:
                    sLenDict.update({s[i]: (sLenDict.get(s[i]) + 1)})
            
            for i in range(len(t)):
                if not tLenDict.get(t[i]):
                    tLenDict.update({t[i]: 1})
                else:
                    tLenDict.update({t[i]: (tLenDict.get(t[i]) + 1)})
            for i in s:
                if sLenDict.get(i) != tLenDict.get(i):
                    return False
        

            return True
        return False