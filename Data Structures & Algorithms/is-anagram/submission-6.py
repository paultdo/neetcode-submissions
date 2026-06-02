class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_map = {}
        hash_map2 = {}

        for c in s:
            if c not in hash_map:
                hash_map[c] = 1
            else:
                hash_map[c] += 1

        for c in t:
            if c not in hash_map2:
                hash_map2[c] = 1
            else:
                hash_map2[c] += 1

        for c in hash_map:
            if c not in hash_map2:
                return False

            if hash_map[c] != hash_map2[c]:
                return False


        return True       

