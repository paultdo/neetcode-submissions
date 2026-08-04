class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_hash = defaultdict(int)
        for c in s1:
            s1_hash[c] += 1
        

        s2_hash = defaultdict(int)

        l, r = 0, 0
        rAddedFlag = True
        while r < len(s2):
            if rAddedFlag:
                s2_hash[s2[r]] += 1
                rAddedFlag = False
            if r - l == len(s1) - 1:
                if s1_hash == s2_hash:
                    return True
                r += 1
                rAddedFlag = True
            elif r - l > len(s1) - 1:
                s2_hash[s2[l]] -= 1
                if s2_hash[s2[l]] == 0:
                    del s2_hash[s2[l]]
                l += 1
            elif r - l < len(s1) - 1:
                r += 1
                rAddedFlag = True
        
        return False