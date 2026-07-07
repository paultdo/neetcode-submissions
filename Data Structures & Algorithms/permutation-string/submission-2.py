class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash_map = {}
        left = 0
        right = 0
        length = 0

        if len(s1) > len(s2):
            return False
        
        for c in s1:
            if c not in hash_map:
                hash_map[c] = 1
            else:
                hash_map[c] += 1
        
        for k in hash_map:
            length += hash_map[k]

        hash_map2 = defaultdict(int)
        while right < len(s2):
            while right - left < length:
                hash_map2[s2[right]] += 1
                right += 1
            
            if hash_map2 == hash_map:
                return True
            else:
                hash_map2[s2[left]] -= 1
                if hash_map2[s2[left]] == 0:
                    del hash_map2[s2[left]]
                left += 1
            
            

        return False

